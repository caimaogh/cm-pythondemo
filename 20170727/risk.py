#!/usr/bin/python
import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import json as jn
import logging as log
import types


def numpyAssetAllocation(inparam):
    paramList = jn.loads(inparam)
    arraySize = len(paramList)
    if arraySize != 3: return 'ERROR_PARAMETER'
    arrayCombW = np.array(paramList[0])
    arrayBenchW = np.array(paramList[1])
    arrayBenchRate = np.array(paramList[2])
    ratValue1 = (arrayCombW - arrayBenchW) * arrayBenchRate
    if type(ratValue1) == type(np.ones(2)):
        retData = jn.dumps(ratValue1.tolist())
    else:
        retData = jn.dumps(ratValue1)
    return retData


def numpyChoiceStock(inparam):
    paramList = jn.loads(inparam)
    arraySize = len(paramList)
    if arraySize != 3: return 'ERROR_PARAMETER'
    arrayCombW = np.array(paramList[0])
    arrayCombRate = np.array(paramList[1])
    arrayBenchRate = np.array(paramList[2])
    ratValue1 = arrayCombW * (arrayCombRate - arrayBenchRate)
    if type(ratValue1) == type(np.ones(2)):
        retData = jn.dumps(ratValue1.tolist())
    else:
        retData = jn.dumps(ratValue1)
    return retData


def numpyInteraction(inparam):
    paramList = jn.loads(inparam)
    arraySize = len(paramList)
    if arraySize != 4: return 'ERROR_PARAMETER'
    arrayCombW = np.array(paramList[0])
    arrayBenchW = np.array(paramList[1])
    arrayCombRate = np.array(paramList[2])
    arrayBenchRate = np.array(paramList[3])
    ratValue1 = (arrayCombW - arrayBenchW) * (arrayCombRate - arrayBenchRate)
    if type(ratValue1) == type(np.ones(2)):
        retData = jn.dumps(ratValue1.tolist())
    else:
        retData = jn.dumps(ratValue1)
    return retData


def attributionK(combRate, benchRate):
    arrayCombRate = np.array(combRate)
    arrayBenchRate = np.array(benchRate)
    retData = (np.log(arrayCombRate + 1) - np.log(arrayBenchRate + 1)) / (arrayCombRate - arrayBenchRate)
    return retData


def attributionKt(combRate, benchRate):
    arrayCombRate = np.array(combRate)
    arrayBenchRate = np.array(benchRate)
    retData = (np.log(arrayCombRate + 1) - np.log(arrayBenchRate + 1)) / (arrayCombRate - arrayBenchRate)
    return retData


def rateMult(rateA):
    rateSum = 1
    rateArray = rateA
    for var in rateArray: rateSum = rateSum * (1 + var)
    rateSum = rateSum - 1
    return rateSum


def rateMultArray(arrayRate):
    rateSum = []
    rateArray = np.array(arrayRate)
    if (rateArray.ndim == 1):
        rateSum = rateMult(rateArray)
    else:
        for var in rateArray:
            rateSum.append(rateMult(var))
    return rateSum



def numpyMultiphaseAssetAllocation():
    # paramList = jn.loads(inparam)
    # arraySize = len(paramList)
    nAxis = None
    # if arraySize != 5: return 'ERROR_PARAMETER'
    # arrayCombW = np.array([[0.9999999999999998,1,1],[0.7967445980676848,0.8462472982218912,0.8579763457163504],[0.05868013860065287,0.06073940516927372,0.0629491480704098],[0.09513734807230557,0.07088736323581245,0.054784865569672256],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0.04943791525935643,0.022125933373022995,0.02428964064356787],[0,0,0]])
    # arrayBenchW = np.array([[1,1,1],[1,1,1],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]])
    # arrayCombRate = np.array([[-0.017687149603551264,-0.001109297231581316,-0.013887833346575378],[-0.023267961559379158,-0.0013805446940402533,-0.01614997490885728],[0.0003334782188224583,0.0005079228521793766,0.000472884936607354],[0.000013638393973502971,0.000054732433492965527,0.00006903557163795426],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]])
    # arrayBenchRate = np.array([[-0.029961697918897145,0.0013125059904356957,-0.012848601551905214],[-0.029961697918897145,0.0013125059904356957,-0.012848601551905214],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]])
    # arrayRootRate = np.array([[-0.029961697918897145,0.0013125059904356957,-0.012848601551905214]])

    ### 20180703-20180710
    # arrayCombW = np.array([[1.0000000000000009,1,1,0.9999999999999998,0.9999999999999998,0.9999999999999998,0.9999999999999998,1],[0.8462472982218912,0.8579763457163505,0.9034284678089731,0.86874654930645,0.86874654930645,0.86874654930645,0.9064027154290013,0.9157326256761409],[0.06073940516927375,0.06294914807040979,0.0667564016855783,0.06218079234106937,0.06218079234106937,0.06218079234106937,0.060777559680411604,0.060578962167383385],[0.07088736323581248,0.05478486556967224,0,0.015148668649031619,0.015148668649031619,0.015148668649031619,0.010566426313551478,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0.022125933373023002,0.024289640643567863,0.029815130505448623,0.05392398970344903,0.05392398970344903,0.05392398970344903,0.02225329857703571,0.02368841215647587],[0,0,0,0,0,0,0,0]])
    # arrayBenchW = np.array([[0.9999999999999999,0.9999999999999999,0.9999999999999999,0.9999999999999999,0.9999999999999999,0.9999999999999999,0.9999999999999999,0.9999999999999999],[0.7973592905532441,0.7973592905532441,0.7973592905532441,0.7973592905532441,0.7973592905532441,0.7973592905532441,0.7973592905532441,0.7973592905532441],[0.202640709446756,0.202640709446756,0.202640709446756,0.202640709446756,0.202640709446756,0.202640709446756,0.202640709446756,0.202640709446756],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])
    # arrayCombRate = np.array([[-0.0011092972315809894,-0.013887833346575812,-0.01438134216720131,0.004719500330491149,0.00000663170316442832,0.000006631653345492303,0.020815765949282534,0.004186464200408049],[-0.0013805446940409194,-0.016149974908856946,-0.016479026158544796,0.005327878514462592,0,0,0.023056800028965707,0.004568039761347675],[0.0005079228521793766,0.000472884936607354,0.00020666064780394677,0.00012809570516703062,0.00010422501841489407,0.00010421419120465458,0.0005671006752820951,0.00020130900865478196],[0.000054732433492965527,0.00006903557163795426,0,0.00006808214285713987,0.00006807750799442402,0.00006807287376298099,-0.00005271038655352278,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])
    # arrayBenchRate = np.array([[0.0011745310487925212,-0.010240961980523185,-0.003907544973232364,0.005923829915230594,0.000019265788796870587,0.000019265788796870587,0.02201381546368798,0.0022262401317191725],[0.001312505990435694,-0.012848601551905226,-0.005120897698653049,0.007404365115781103,0,0,0.027570326185596458,0.0027067531328704157],[0.0006316213744082926,0.00001968921998037615,0.0008668069868138812,0.0000981569772850092,0.00009507363475714983,0.00009507363475714983,0.00014982051781280834,0.00033549711791110626],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])
    # arrayRootRate = np.array([[0.0011745310487925212,-0.010240961980523185,-0.003907544973232364,0.005923829915230594,0.000019265788796870587,0.000019265788796870587,0.02201381546368798,0.0022262401317191725]])

    ### 20180703-20180710
    arrayCombW = np.array([[1.0000000000000009,1,1,0.9999999999999998],[0.8462472982218912,0.8579763457163505,0.9034284678089731,0.86874654930645],[0.06073940516927375,0.06294914807040979,0.0667564016855783,0.06218079234106937],[0.07088736323581248,0.05478486556967224,0,0.015148668649031619],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0.022125933373023002,0.024289640643567863,0.029815130505448623,0.05392398970344903],[0,0,0,0]])
    arrayBenchW = np.array([[0.9999999999999999,0.9999999999999999,0.9999999999999999,0.9999999999999999],[0.7973592905532441,0.7973592905532441,0.7973592905532441,0.7973592905532441],[0.202640709446756,0.202640709446756,0.202640709446756,0.202640709446756],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    arrayCombRate = np.array([[-0.0011092972315809894,-0.013887833346575812,-0.01438134216720131,0.004719500330491149],[-0.0013805446940409194,-0.016149974908856946,-0.016479026158544796,0.005327878514462592],[0.0005079228521793766,0.000472884936607354,0.00020666064780394677,0.00012809570516703062],[0.000054732433492965527,0.00006903557163795426,0,0.00006808214285713987],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    arrayBenchRate = np.array([[0.0011745310487925212,-0.010240961980523185,-0.003907544973232364,0.005923829915230594],[0.001312505990435694,-0.012848601551905226,-0.005120897698653049,0.007404365115781103],[0.0006316213744082926,0.00001968921998037615,0.0008668069868138812,0.0000981569772850092],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    arrayRootRate = np.array([[0.0011745310487925212,-0.010240961980523185,-0.003907544973232364,0.005923829915230594]])

    cRate = rateMultArray(arrayCombRate)
    print("cRate",cRate)
    bRate = rateMultArray(arrayBenchRate)
    print("bRate",bRate)
    k = attributionK(cRate, bRate)
    arrayK = np.array(k)
    print("arrayK", arrayK)
    if arrayK.size > 1: arrayK.shape = (arrayK.size, 1)
    print("arrayCombRate", arrayCombRate)
    print("arrayBenchRate", arrayBenchRate)
    Kt = attributionKt(arrayCombRate, arrayBenchRate)
    print("Kt", Kt)
    aiu = (arrayCombW - arrayBenchW)
    aid = (arrayBenchRate - arrayRootRate)
    print("aiu", aiu)
    print("aid", aid)
    Ai = (arrayCombW - arrayBenchW) * (arrayBenchRate - arrayRootRate)
    print("Ai", Ai)

    if (Ai.ndim > 1): nAxis = 1
    print("nAxis=",nAxis)
    print("Kt / arrayK * Ai===", (Kt / arrayK * Ai))
    ratValue = np.sum(Kt / arrayK * Ai, axis=nAxis)
    print("ratValue=", ratValue)
    ratValue=np.nan_to_num(ratValue)
    if type(ratValue) == type(np.ones(2)):
        retData = jn.dumps(ratValue.tolist())
    else:
        retData = jn.dumps(ratValue)
    return retData

result = numpyMultiphaseAssetAllocation();
print(result)

