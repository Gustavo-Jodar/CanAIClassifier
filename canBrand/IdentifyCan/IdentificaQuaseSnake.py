#bibliotecas
import math
import numpy as np
import skimage.data as data
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color
from skimage import io
import algort_KNN as knn_source

import sys

def circle_points(resolution, center, radius):
    """
    Generate points which define a circle on an image.
    Centre refers to the centre of the circle
    """
    radians = np.linspace(0, 2*np.pi, resolution)
    c = center[1] + radius*np.cos(radians)#polar co-ordinates
    r = center[0] + radius*np.sin(radians)

    return np.array([c, r]).T# Exclude last point because a closed path should not have duplicate points

#carrega o nome da imagem passado como argumento
image_name = sys.argv[1]

image = io.imread("/var/www/html/gj/CanAIClassifier/uploads/{}".format(image_name))
copy_image = image

points = circle_points(200, [625, 625], 550)[:-1]
snake = seg.active_contour(color.rgb2gray(copy_image), points,alpha=0.02, w_edge=0, w_line=1, coordinates='rc')
snake = snake.astype(int)

image = image[int(snake[:,0].min()):int(snake[:,0].max()), int(snake[:,1].min()):int(snake[:,1].max())]


media_red_amostra = image[:,:,0].mean()
media_green_amostra = image[:,:,1].mean()
media_blue_amostra = image[:,:,2].mean()

DP_red = image[:,:,0].std()
DP_green = image[:,:,1].std()
DP_blue = image[:,:,2].std()

Dados = [{}]
Dados = [
{'media_R':85.98582, 'media_G':122.19920, 'media_B':102.48774,'DP_red':84.33640,'DP_green':68.30786,'DP_blue':73.23432,'latinha': 1},
{'media_R':94.83658, 'media_G':129.18515, 'media_B':110.36065,'DP_red':82.72893,'DP_green':69.22852,'DP_blue':74.11717,'latinha': 1},
{'media_R':99.50044, 'media_G':125.71804, 'media_B':108.19387,'DP_red':78.77405,'DP_green':64.03609,'DP_blue':68.62082,'latinha': 1},
{'media_R':100.98715, 'media_G':114.34737, 'media_B':100.78860,'DP_red':79.98251,'DP_green':63.01164,'DP_blue':69.33621,'latinha': 1},
{'media_R':91.36842, 'media_G':128.14528, 'media_B':110.24382,'DP_red':90.40293,'DP_green':67.91175,'DP_blue':75.86753,'latinha': 1},
{'media_R':142.74549, 'media_G':158.66192, 'media_B':149.86103,'DP_red':80.71936,'DP_green':59.26273,'DP_blue':64.62993,'latinha': 1},
{'media_R':131.90545, 'media_G':148.18803, 'media_B':137.61427,'DP_red':76.31373,'DP_green':57.50207,'DP_blue':63.34759,'latinha': 1},
{'media_R':102.88290, 'media_G':133.22799, 'media_B':102.64812,'DP_red':101.79248,'DP_green':77.59869,'DP_blue':85.54655,'latinha': 1},
{'media_R':118.68153, 'media_G':118.22961, 'media_B':102.91597,'DP_red':98.86673,'DP_green':90.35033,'DP_blue':97.55273,'latinha': 1},
{'media_R':102.88290, 'media_G':133.22799, 'media_B':102.64812,'DP_red':101.79248,'DP_green':77.59869,'DP_blue':85.54655,'latinha': 1},
{'media_R':144.38596, 'media_G':130.85003, 'media_B':116.85577,'DP_red':54.02771,'DP_green':60.20624,'DP_blue':66.39692,'latinha': 2},
{'media_R':155.11561, 'media_G':136.67822, 'media_B':122.31311,'DP_red':56.44935,'DP_green':67.87832,'DP_blue':75.21661,'latinha': 2},
{'media_R':146.50292, 'media_G':131.64933, 'media_B':118.43943,'DP_red':59.94503,'DP_green':69.30134,'DP_blue':76.40255,'latinha': 2},
{'media_R':150.12457, 'media_G':129.87065, 'media_B':112.90831,'DP_red':51.61295,'DP_green':62.24296,'DP_blue':70.49375,'latinha': 2},
{'media_R':138.78266, 'media_G':120.74069, 'media_B':104.92778,'DP_red':47.93385,'DP_green':56.51394,'DP_blue':64.43746,'latinha': 2},
{'media_R':161.75678, 'media_G':147.70463, 'media_B':140.06046,'DP_red':46.28441,'DP_green':57.71837,'DP_blue':62.80033,'latinha': 2},
{'media_R':147.52371, 'media_G':120.44547, 'media_B':101.31493,'DP_red':46.47903,'DP_green':58.92603,'DP_blue':63.29908,'latinha': 2},
{'media_R':201.59165, 'media_G':172.71094, 'media_B':144.37693,'DP_red':51.59032,'DP_green':71.40573,'DP_blue':89.06909,'latinha': 2},
{'media_R':192.74543, 'media_G':171.96742, 'media_B':164.52996,'DP_red':50.28361,'DP_green':73.81270,'DP_blue':80.38282,'latinha': 2},
{'media_R':192.74543, 'media_G':171.96742, 'media_B':164.52996,'DP_red':50.28361,'DP_green':73.81270,'DP_blue':80.38282,'latinha': 2},
{'media_R':76.38529, 'media_G':107.03754, 'media_B':142.32812,'DP_red':84.90520,'DP_green':71.20323,'DP_blue':57.37528,'latinha': 3},
{'media_R':88.20759, 'media_G':110.58743, 'media_B':135.66715,'DP_red':78.04023,'DP_green':65.51143,'DP_blue':53.78887,'latinha': 3},
{'media_R':88.24081, 'media_G':112.99809, 'media_B':140.20449,'DP_red':81.82890,'DP_green':65.52205,'DP_blue':49.76849,'latinha': 3},
{'media_R':91.18785, 'media_G':117.03011, 'media_B':146.33648,'DP_red':85.31982,'DP_green':67.93317,'DP_blue':51.30014,'latinha': 3},
{'media_R':91.18785, 'media_G':117.03011, 'media_B':146.33648,'DP_red':85.31982,'DP_green':67.93317,'DP_blue':51.30014,'latinha': 3},
{'media_R':135.89475, 'media_G':152.11179, 'media_B':173.82549,'DP_red':87.61575,'DP_green':67.19403,'DP_blue':44.83650,'latinha': 3},
{'media_R':123.60554, 'media_G':138.09206, 'media_B':160.12075,'DP_red':73.22779,'DP_green':56.20470,'DP_blue':45.29913,'latinha': 3},
{'media_R':73.58709, 'media_G':122.31990, 'media_B':175.29201,'DP_red':80.82390,'DP_green':56.85630,'DP_blue':36.42328,'latinha': 3},
{'media_R':59.10414, 'media_G':93.65309, 'media_B':150.12225,'DP_red':89.99574,'DP_green':73.11618,'DP_blue':56.71612,'latinha': 3},
{'media_R':59.10414, 'media_G':93.65309, 'media_B':150.12225,'DP_red':89.99574,'DP_green':73.11618,'DP_blue':56.71612,'latinha': 3},
{'media_R':146.82627, 'media_G':103.11766, 'media_B':92.94183,'DP_red':52.07370,'DP_green':72.22779,'DP_blue':74.58189,'latinha': 4},
{'media_R':160.42135, 'media_G':102.46607, 'media_B':92.33730,'DP_red':59.56229,'DP_green':83.33135,'DP_blue':84.66054,'latinha': 4},
{'media_R':148.23567, 'media_G':99.48473, 'media_B':87.21493,'DP_red':48.10822,'DP_green':67.62768,'DP_blue':68.98392,'latinha': 4},
{'media_R':147.58312, 'media_G':108.46938, 'media_B':94.61890,'DP_red':46.75538,'DP_green':65.94917,'DP_blue':69.88424,'latinha': 4},
{'media_R':172.74511, 'media_G':115.96119, 'media_B':101.49144,'DP_red':45.60988,'DP_green':73.13012,'DP_blue':75.68287,'latinha': 4},
{'media_R':171.92774, 'media_G':148.29328, 'media_B':143.65201,'DP_red':45.73366,'DP_green':63.96665,'DP_blue':66.06583,'latinha': 4},
{'media_R':162.02270, 'media_G':135.07279, 'media_B':117.89455,'DP_red':43.64781,'DP_green':60.66933,'DP_blue':68.79266,'latinha': 4},
{'media_R':205.61196, 'media_G':126.36378, 'media_B':104.24616,'DP_red':48.25982,'DP_green':88.56408,'DP_blue':93.16068,'latinha': 4},
{'media_R':208.94272, 'media_G':131.74858, 'media_B':113.30774,'DP_red':43.94625,'DP_green':83.61913,'DP_blue':85.32258,'latinha': 4},
{'media_R':180.76000, 'media_G':125.40504, 'media_B':99.51658,'DP_red':44.22247,'DP_green':68.99832,'DP_blue':75.58107,'latinha': 4},
{'media_R':166.28865, 'media_G':156.20971, 'media_B':141.56106,'DP_red':49.92513,'DP_green':53.18597,'DP_blue':55.38889,'latinha': 5},
{'media_R':161.93114, 'media_G':151.65928, 'media_B':134.12512,'DP_red':41.70010,'DP_green':45.29660,'DP_blue':48.90700,'latinha': 5},
{'media_R':160.84481, 'media_G':150.58172, 'media_B':133.56659,'DP_red':40.05572,'DP_green':43.64034,'DP_blue':48.59223,'latinha': 5},
{'media_R':163.02249, 'media_G':152.69249, 'media_B':136.86490,'DP_red':42.70353,'DP_green':46.35340,'DP_blue':51.28828,'latinha': 5},
{'media_R':145.83302, 'media_G':135.90249, 'media_B':121.00951,'DP_red':44.42882,'DP_green':47.28280,'DP_blue':50.31498,'latinha': 5},
{'media_R':155.58763, 'media_G':149.78032, 'media_B':142.33973,'DP_red':47.25511,'DP_green':48.96514,'DP_blue':50.81634,'latinha': 5},
{'media_R':153.95929, 'media_G':144.15058, 'media_B':129.46169,'DP_red':43.99891,'DP_green':49.15154,'DP_blue':56.69898,'latinha': 5},
{'media_R':214.43322, 'media_G':208.05391, 'media_B':185.68907,'DP_red':58.02383,'DP_green':59.62255,'DP_blue':69.76212,'latinha': 5},
{'media_R':197.99712, 'media_G':194.08737, 'media_B':159.64021,'DP_red':50.99187,'DP_green':54.01579,'DP_blue':64.74474,'latinha': 5},
{'media_R':194.14073, 'media_G':185.25117, 'media_B':167.34050,'DP_red':53.84076,'DP_green':57.59712,'DP_blue':66.47066,'latinha': 5},
{'media_R':124.45728, 'media_G':91.25050, 'media_B':89.18296,'DP_red':55.44460,'DP_green':66.15682,'DP_blue':65.13439,'latinha': 6},
{'media_R':139.97865, 'media_G':125.14405, 'media_B':123.99999,'DP_red':63.94007,'DP_green':71.88482,'DP_blue':70.29694,'latinha': 6},
{'media_R':138.70977, 'media_G':127.68820, 'media_B':126.57469,'DP_red':61.30142,'DP_green':68.05216,'DP_blue':67.19374,'latinha': 6},
{'media_R':136.30278, 'media_G':117.42559, 'media_B':116.55950,'DP_red':61.55279,'DP_green':69.10229,'DP_blue':68.01407,'latinha': 6},
{'media_R':140.32765, 'media_G':123.76556, 'media_B':122.55854,'DP_red':57.87872,'DP_green':66.08074,'DP_blue':64.91699,'latinha': 6},
{'media_R':171.10436, 'media_G':151.52692, 'media_B':150.98015,'DP_red':54.14665,'DP_green':71.35570,'DP_blue':70.86001,'latinha': 6},
{'media_R':163.25794, 'media_G':147.14747, 'media_B':145.89010,'DP_red':52.63767,'DP_green':65.53861,'DP_blue':65.00029,'latinha': 6},
{'media_R':169.99803, 'media_G':99.34737, 'media_B':101.27063,'DP_red':49.30090,'DP_green':81.59598,'DP_blue':80.40391,'latinha': 6},
{'media_R':169.99803, 'media_G':99.34737, 'media_B':101.27063,'DP_red':49.30090,'DP_green':81.59598,'DP_blue':80.40391,'latinha': 6},
{'media_R':221.41417, 'media_G':143.99139, 'media_B':147.09934,'DP_red':31.72215,'DP_green':105.07585,'DP_blue':103.92281,'latinha': 6},
{'media_R':165.19291, 'media_G':148.65518, 'media_B':136.85269,'DP_red':49.23072,'DP_green':57.33756,'DP_blue':65.30628,'latinha': 7},
{'media_R':155.48697, 'media_G':148.31645, 'media_B':144.50348,'DP_red':47.92356,'DP_green':52.96541,'DP_blue':53.54140,'latinha': 7},
{'media_R':155.13165, 'media_G':151.22801, 'media_B':148.83802,'DP_red':48.20401,'DP_green':48.97670,'DP_blue':47.81076,'latinha': 7},
{'media_R':155.11365, 'media_G':145.53791, 'media_B':139.46841,'DP_red':42.18386,'DP_green':49.06709,'DP_blue':51.17539,'latinha': 7},
{'media_R':155.02523, 'media_G':144.61027, 'media_B':137.13297,'DP_red':43.04804,'DP_green':48.86029,'DP_blue':52.93686,'latinha': 7},
{'media_R':151.51999, 'media_G':144.23322, 'media_B':138.74704,'DP_red':47.29235,'DP_green':48.78997,'DP_blue':50.65714,'latinha': 7},
{'media_R':145.16860, 'media_G':138.23401, 'media_B':133.91161,'DP_red':47.10540,'DP_green':50.28057,'DP_blue':50.72245,'latinha': 7},
{'media_R':234.74942, 'media_G':234.12064, 'media_B':234.49438,'DP_red':48.49409,'DP_green':49.70846,'DP_blue':48.43757,'latinha': 7},
{'media_R':210.60988, 'media_G':206.75304, 'media_B':189.42428,'DP_red':75.36940,'DP_green':70.20389,'DP_blue':83.60899,'latinha': 7},
{'media_R':210.60988, 'media_G':206.75304, 'media_B':189.42428,'DP_red':75.36940,'DP_green':70.20389,'DP_blue':83.60899,'latinha': 7},
{'media_R':168.92080, 'media_G':138.08293, 'media_B':128.49492,'DP_red':41.80930,'DP_green':55.03475,'DP_blue':57.30887,'latinha': 8},
{'media_R':166.54792, 'media_G':129.62381, 'media_B':119.20383,'DP_red':36.21904,'DP_green':55.15346,'DP_blue':58.79743,'latinha': 8},
{'media_R':170.05133, 'media_G':132.47014, 'media_B':123.69490,'DP_red':36.38155,'DP_green':56.62583,'DP_blue':59.76521,'latinha': 8},
{'media_R':164.90389, 'media_G':137.38001, 'media_B':129.77721,'DP_red':33.46015,'DP_green':52.15123,'DP_blue':54.33979,'latinha': 8},
{'media_R':158.83475, 'media_G':133.55953, 'media_B':122.91922,'DP_red':37.97196,'DP_green':51.51994,'DP_blue':54.67581,'latinha': 8},
{'media_R':188.50371, 'media_G':168.51204, 'media_B':162.40476,'DP_red':35.99415,'DP_green':53.89063,'DP_blue':57.55842,'latinha': 8},
{'media_R':157.79464, 'media_G':139.73046, 'media_B':128.03455,'DP_red':42.01695,'DP_green':54.14158,'DP_blue':60.41299,'latinha': 8},
{'media_R':207.37640, 'media_G':151.58490, 'media_B':130.56634,'DP_red':50.41207,'DP_green':84.15902,'DP_blue':91.56526,'latinha': 8},
{'media_R':207.37640, 'media_G':151.58490, 'media_B':130.56634,'DP_red':50.41207,'DP_green':84.15902,'DP_blue':91.56526,'latinha': 8},
{'media_R':176.04665, 'media_G':151.50946, 'media_B':144.18217,'DP_red':61.19292,'DP_green':83.16216,'DP_blue':88.46462,'latinha': 8},
]

resultado = knn_source.KNN(Dados, media_red_amostra, media_green_amostra, media_blue_amostra,
DP_red, DP_green, DP_blue)

if  (resultado == 1):
    print("Guaraná")
elif(resultado == 2):
    print("Amstel")
elif(resultado == 3):
    print("Tônica")
elif(resultado == 4):
    print("Brahma")
elif(resultado == 5):
    print("Boemia")
elif(resultado == 6):
    print("Coca-Cola Coffee")
elif(resultado == 7):
    print("original")
elif(resultado == 8):
    print("Petra")



