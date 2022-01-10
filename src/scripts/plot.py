import include_parent_path
from matplotlib import pyplot as plt

y_psnr = [17.084534849070053, 17.085611445129462, 17.85586801812742, 17.76168484959518, 
17.470691094112997, 17.65381312055669, 17.444905143446547, 17.743212612673467, 17.994097119009208,
17.837358302495993, 17.792738537246336, 18.04743288963593, 17.98041131225981, 17.826892431402026, 
17.838954897888502, 17.9251180377915, 17.551504625249986, 17.617314130230984, 17.8133110702289, 
17.870732833815282, 18.264754202360955, 17.766248000407543, 17.983447981452958, 18.066010305621976, 
17.933023756564253, 17.96434529135319, 18.132788634408648, 17.95558455005914, 17.655377096657134, 
17.700519911675098, 17.854424465627915, 18.21851529392301, 18.15981730082053, 17.57375675681852, 
18.18180050447043, 17.970418167254536, 17.934343420383456, 17.934390450889648, 17.912328429143862, 
17.9334986562615, 18.096486773454572, 17.991658374281485, 17.977498054717476, 18.068607128755485, 
18.006226258296394, 17.891735172558516, 17.76621154630568, 17.929544247533606, 18.01742261345561, 
17.775450404592217, 18.15633087439761, 17.710449800489513, 18.381499824706612, 18.077421293247784, 
17.928896836602608, 17.98134237407197, 17.93585256450699, 17.848002329542446, 18.11858514814925, 
18.156224600104174, 17.87740407182354, 18.095296177072388, 17.93519896513856, 17.656492609964634, 
17.80683271528373, 18.28975031763114, 18.002825949704988, 18.035466029369587, 17.954189158826807, 
17.707995549401343, 18.092871110711517, 18.056694195082095, 17.852663926255815, 18.085734949681456, 
17.713214424872145, 17.987099545197132, 17.74638959599732, 17.716351112270946, 17.618787962606675, 
17.811681594616996, 18.05568949022336, 18.146136266613635, 17.992603027372496, 18.123260715016944, 
18.156593809864187, 17.827058096472772, 17.75557859622199, 17.486794661112093, 17.954050474297908, 
18.09166166020721, 18.01154285202651, 17.930688457950797, 18.01949471118934, 18.031077007007028, 
17.888596567594682, 17.788697592241604, 17.965826966998524, 17.55531052886672, 17.740333574267666, 
18.163552100109353, 17.82953587813494, 17.716897495830207, 18.06083494743955, 17.63465852213565, 
18.118159305864246, 17.864827993236485, 18.012184449835054, 17.733621365515486, 18.118498856149206, 
17.913870137352678, 17.751487533176327, 17.87635429905203, 17.811536196805182, 18.055364579758955, 
17.976029265350213, 17.737936572752474, 17.95068377728591, 17.828310961694626, 18.031569371779526, 
18.000358316851553, 17.662988233572534, 18.008392984037318, 17.881399319050647, 18.37341129228245, 
18.19440923650595, 18.118978448027264, 17.725396239179982, 17.849988681009588, 18.226862039277854, 
17.87464389709568, 17.913248644776765, 17.824645414290192, 17.64301908185794, 17.91679287685475, 
17.98862858913933, 17.79645997022785, 18.031746830941792, 18.036741736743245, 18.200898763258447, 
18.17119207677121, 18.011093486090246, 18.1139525940395, 17.952153094184975, 18.060769994075603, 
17.910054148944386, 18.095112712111696, 17.883494658523713, 18.089921948079038, 17.97393007586745, 
18.00373491234456, 18.02357780891442, 18.08890971015024, 17.905734528357417, 17.946433916967074,
17.966711254095838, 17.843546218951168, 17.934276750633092, 18.124290027925177, 17.794981303844438, 
17.898963419630842, 17.979870303236297, 17.990579388725205, 18.11585632178735, 17.914342974910586,
18.09806570082745, 17.963078704633855, 17.864433836201908, 17.97610183387531, 18.12131655767946, 
17.95389616018674, 17.89269432465608, 17.87295695194527, 17.794333700248682, 17.90231326840217, 
18.079361831168168, 17.83531227040793, 18.01818073253676, 17.840862496467107, 18.166054125215673, 
18.036728333792908, 18.04085149069995, 17.95704286038931, 18.04487891801451, 17.870499814048895,
18.077529249451064, 17.91986415922927, 17.844953653625193, 18.00943055459046, 17.964551079232294, 
17.976877505301882, 17.985226165680263, 18.072058093885417, 17.980686680164812, 17.975798705289872, 
17.982018350492044, 17.982725190381295, 18.018886482952716, 17.97155309274717, 18.004038125734958, 
17.999057924658725, 17.999057924658732] 
y_psnr_mse = [
    17.072432852799285, 16.97351994740464, 17.466108589644723, 17.3031920434327, 17.68440347208907, 
    17.71967312211237, 17.808383943071778, 17.461159221138807, 17.422443996219513, 17.554694891719322, 
    17.742290098086162, 17.621334491690874, 17.61509838296735, 17.81853327884335, 17.58382554211101, 
    17.597369640047425, 17.53333838454254, 17.992750999120318, 17.646121958538483, 17.43324325937041, 
    17.738502677007418, 17.81265592026159, 17.75243513842562, 17.69644459955801, 17.58886337395522, 
    17.803361374754537, 17.996331638733896, 17.54406068171428, 17.629614620294678, 17.48445183181691, 
    17.890605684210517, 17.698348628590747, 17.671159889895335, 17.350837368549744, 17.859219188779655, 
    17.888527345197005, 17.52164414548044, 17.608709241902474, 17.652892081908796, 17.656904427963465, 
    17.639256622906892, 17.72958015519842, 17.577324327484856, 17.65806385278701, 17.481237264504514, 
    17.508269616328487, 17.520020805193095, 17.67230260525459, 17.806335640485536, 17.694978665695185, 
    17.5681506063613, 17.714865596198738, 17.438716726058942, 17.615699729429725, 17.435818715644952, 
    17.588583990883762, 17.47011975218204, 17.633580086565026, 17.378151484304844, 17.99277067431077, 
    17.90586197338299, 17.426145266437356, 17.822268726692784, 17.60768421405087, 17.38648238662073, 
    17.483696637495054, 17.404128754001217, 17.55427363449373, 17.756117176536797, 17.664577881724302, 
    17.9366570323366, 17.559300202939117, 18.223648741315532, 17.73169430824579, 17.673140883035156, 
    17.563806928562034, 17.55959619120137, 17.868581889599167, 17.88749598474671, 17.918692245604174, 
    18.10848588101883, 17.78007459404428, 17.492431735842146, 18.048085291483876, 17.704134385835815, 
    17.749168512370872, 17.86040733200687, 17.819255757551165, 17.730513798081454, 17.74869410969791, 
    17.974356294026386, 17.719417265639116, 18.00024580459332, 17.57986465799487, 17.910804102674632, 
    17.520589024088977, 17.497738178941514, 17.765734454924704, 17.928590948385157, 17.317563405491036, 
    17.37612318719673, 17.802188224942455, 17.70744904531303, 17.636048660142357, 17.949932147196826, 
    17.333078686066916, 17.897026266307442, 17.59273483484528, 17.908682912552116, 18.042419197569334, 
    17.986598601637326, 17.626832664115412, 17.723068176790218, 17.975617136584553, 17.697466553561224, 
    17.66536540746693, 17.76186209348852, 17.73609740999127, 17.94917067602975, 17.501851536553875, 
    17.573388109548507, 17.5952546397226, 18.089374272922104, 18.01697046847756, 17.71168274650232, 
    17.889597387587592, 17.729896837605185, 18.0835321092069, 17.76645854265383, 17.919523239329454, 
    17.838954197908894, 17.785846004863835, 18.08552572207832, 17.87493289491126, 17.673489887305706, 
    17.897094387179322, 17.997718689192794, 17.780927201958345, 17.757519683466718, 17.76529659678683, 
    17.85615744381694, 17.905544006413535, 17.591181781511278, 17.678921371085828, 18.275023474428473, 
    17.818820246572006, 17.894250950795847, 17.80384966877567, 17.90765449868201, 17.639348811126336, 
    18.132757420272384, 17.81415779073268, 18.029892093460475, 17.864885723688214, 17.528411340847796, 
    17.733979746619216, 17.82306988153861, 17.710354464795827, 17.70082153386619, 17.860068303134394, 
    17.869583943645114, 17.817770654023445, 17.99338021937676, 17.60467530603602, 17.81673331607611, 
    17.79880167440418, 17.673193657768635, 17.783791004551247, 17.936566017255586, 17.732620674573703, 
    17.840136243293408, 18.01025570179337, 17.982055894252156, 17.897097448698414, 17.813867181395747, 
    17.68018748750397, 17.797111046884414, 17.815460948972508, 17.670045202851433, 17.779031968558776, 
    17.97308712515689, 17.987666875511916, 17.846434417939946, 17.796312778093093, 17.810990851231324, 
    17.841058025494107, 17.721365714979207, 17.809093690270636, 17.699266610934757, 17.733242683174314, 
    17.865972603363097, 17.790883501868, 17.805647390200264, 17.890570939590702, 17.774353159323883, 
    17.876545254677346, 17.826147104252072, 17.8152896397034, 17.82754359252114, 17.827543592521174
]
y_psnr_ours = [
    18.29097657212114, 18.222122824610942, 18.705699801169438, 18.923536053192837, 19.0354605399592, 
    19.11516444383207, 19.259233448671875, 19.25510387794595, 19.39708191659556, 19.685185471479073, 
    19.393785699998585, 19.696928483074682, 19.742537704872277, 19.652263113858123, 19.825688944295905, 
    19.62207791462246, 19.74597898988577, 19.828390594118176, 19.617623924996657, 19.68256516102716, 
    19.602826751571058, 19.910640363610657, 19.84709958722036, 19.882115504140938, 19.70633160780093, 
    19.857561526978117, 19.753295714269413, 19.943823782192794, 19.868245171623638, 20.203550314165, 
    19.812611942269566, 19.994382157779373, 19.82295214216816, 19.92188353876202, 20.200685398152363, 
    19.897302666470292, 19.98391261266185, 19.955055950172866, 19.982139748506917, 19.836544807557043, 
    19.95897801410967, 20.143559458867475, 20.164655825622106, 20.24271140933378, 20.238308870104966, 
    20.153836644510726, 19.91743077547691, 19.951334885431336, 20.07713283078901, 20.021794873794576, 
    20.036073062632934, 19.990489076474155, 20.253812967779453, 20.049550784478495, 20.07278567233259, 
    19.9876029985492, 20.33542870291628, 19.972082060577062, 20.16301720769952, 20.233364150095827, 
    20.1376940292487, 20.276914121699427, 20.120376735599013, 20.156527767956042, 20.163078370737292, 
    20.159985760894887, 20.086046179873033, 20.05337914565434, 20.191096486822822, 20.22917104575098, 
    20.204312204321624, 20.035558795134456, 20.096603169895605, 20.176494414306664, 20.303943171120814, 
    20.095484286762858, 20.300286092104415, 20.24827168150786, 20.378598988629975, 20.33123579379003, 
    20.33285881038967, 20.363307297171897, 20.35749424116876, 20.37214746964277, 20.347117820851885, 
    20.370621450646652, 20.31453732078904, 20.251069072193825, 20.22723377487335, 20.37962637754211, 
    20.2597252268379, 20.357063227810748, 20.33538454085992, 20.33517052497763, 20.233775365915136, 
    20.45214517992758, 20.35775579547619
]
y_ssim = [0.5289066436366504, 0.5174738705572721, 0.5425900381952273, 0.5402147280135136, 
0.5268520982678883, 0.5331499073659794, 0.5299768790060017, 0.5390139803794719, 0.5482727152823273,
0.5435409406149337, 0.5360673753677548, 0.5506037893595372, 0.5443035204597071, 0.5415022576769355, 
0.5397581764599948, 0.5404325200173675, 0.5318439860992464, 0.5348998069789647, 0.5412671494629454, 
0.5403110041461744, 0.556207686914153, 0.5400445197057825, 0.5460484149795239, 0.5489634877066986, 
0.5455955170888127, 0.5435170547814682, 0.5549033739849102, 0.5417425743460378, 0.5362002756945274, 
0.5371681790834189, 0.5427049933251814, 0.5531570556050057, 0.5556396054664294, 0.5305553187623407, 
0.5556637670398783, 0.5452139480407037, 0.5480968952290255, 0.5456588080509501, 0.5436974420316162, 
0.54641746109308, 0.5520501879942006, 0.5466568380404401, 0.5470643848930773, 0.5483414650019154, 
0.5484249799362889, 0.543744469996506, 0.5377704128041267, 0.5440210219440574, 0.5481334948945714, 
0.5371312190137746, 0.5525838914724455, 0.5356676945915896, 0.5637174318355186, 0.5483399129593739, 
0.5443498748047004, 0.5471151438873574, 0.5449558791576632, 0.5435215596669559, 0.5525495799851865, 
0.5490740593109565, 0.5423793052878438, 0.5507442782244498, 0.5425039084342984, 0.5356852091886231, 
0.5411210888501452, 0.5581980041002256, 0.5477151947921699, 0.5480822147098421, 0.5462164330901057, 
0.5379959433102034, 0.546447969130422, 0.5492312870768493, 0.5428715029125603, 0.5474107802148195, 
0.5351264974131182, 0.5421274914383777, 0.539617947476017, 0.536092154942181, 0.530946191574663, 
0.5389830966562545, 0.5481581015613763, 0.5545504611585861, 0.5469458543794523, 0.5478910329049389, 
0.5538061949237955, 0.5394658660256612, 0.5379875098427395, 0.5315065841344911, 0.5449274675900418, 
0.5480983325897536, 0.5461891662492264, 0.5439469396987657, 0.5469492345124706, 0.5471858767811154, 
0.5424143117491932, 0.5409324553794823, 0.5450104441310233, 0.5318767725534551, 0.5375170110379386, 
0.5519560403779713, 0.5412110442269399, 0.5352742514362568, 0.5455775087378697, 0.5347789416483508, 
0.550959582382478, 0.5412107088657654, 0.5480864859502961, 0.5362032174744412, 0.5515347691684542, 
0.5394578779169553, 0.540376739703147, 0.5400131600714869, 0.5400993451405766, 0.5462594933454461, 
0.5409025255950052, 0.539306406497207, 0.5443287100516165, 0.5388089294207357, 0.5464955175191917, 
0.5490119542288641, 0.5338395066424002, 0.5475736532669611, 0.5424465026083858, 0.5612166563343165, 
0.5511750328604116, 0.5519635839361544, 0.5367336563094275, 0.5396310802731353, 0.5519098066813584, 
0.540721019952176, 0.5426955425926552, 0.54014336354675, 0.5356734235055023, 0.543158296835226, 
0.5435331507571601, 0.5391588640320776, 0.5471749443347504, 0.5469984507250074, 0.5545754434241881, 
0.5527211398524381, 0.5467255724294973, 0.5496789461627747, 0.542653999064042, 0.5472111211653871, 
0.5420549313825043, 0.5496827034842148, 0.5407165009488183, 0.5476155258358041, 0.5443065020053899, 
0.5442556485961184, 0.5449253962830711, 0.5471841717116487, 0.540492094828682, 0.5441873645431042, 
0.5433485125506534, 0.5393701984865445, 0.5438047889635994, 0.5497622286198882, 0.5377861630141442, 
0.5416875276613176, 0.5442388272652875, 0.5450021324665402, 0.5502477211291738, 0.5416174516969505, 
0.5482556196746876, 0.5441376242809275, 0.5397339403454334, 0.545126893548129, 0.5502698223419777,
0.5434313517181221, 0.5410441369814397, 0.540089949349626, 0.5361398618404718, 0.5410623538725373, 
0.547129709335513, 0.5400400494950037, 0.5455892130755359, 0.5392402194328957, 0.550884658306606, 
0.5459355923945733, 0.5461421073683886, 0.543004114061156, 0.5452507472454775, 0.5407369608750688, 
0.547357419585538, 0.5420274923057496, 0.5396614453126809, 0.5445884459643998, 0.5431151136325479, 
0.543596467231655, 0.543729639378069, 0.5472934397085689, 0.543832427047851, 0.5433246499030934, 
0.5435048751964657, 0.5437361484440175, 0.5453388047173523, 0.543422711159699, 0.5445609730960549, 
0.5444041446533983, 0.5444041446533983]
y_ssim_mse = [
    0.5135584132144941, 0.5091291969350088, 0.5264090780337506, 0.5207899148549225, 0.5337039150608984, 
    0.534143719071336, 0.5384657641210793, 0.5271419181761736, 0.5250120188837327, 0.5255903171568248, 
    0.5349281448324743, 0.5318025966301684, 0.5334100549258995, 0.5412005131787542, 0.5285292264906807, 
    0.531592855722668, 0.5319787039252648, 0.545632106504478, 0.5358678296383498, 0.5236421406552749, 
    0.5376931338797843, 0.5410308631814248, 0.5356514982396717, 0.5351883784477361, 0.5333472815356395, 
    0.538451342104396, 0.5458082625285369, 0.5277747095204419, 0.5309060228016476, 0.5295062233286837, 
    0.5453913329938892, 0.5352075160993347, 0.5327991787549113, 0.5229564523827145, 0.539604275778719, 
    0.5392030971382245, 0.530560229195939, 0.5321642567706872, 0.5305210552379562, 0.5336457065726972, 
    0.5352138713047385, 0.5377984445654256, 0.5311277775942999, 0.5340561955580482, 0.5237670957198446, 
    0.5296868361846024, 0.5307783699593167, 0.5315948652824284, 0.541471454060464, 0.5340181141290928, 
    0.5309299055558889, 0.5387750422778615, 0.525365270307568, 0.5313716408379165, 0.5275768418397981, 
    0.5292958203774341, 0.5296638382197828, 0.5371280056512141, 0.5296931478112903, 0.5493350876387689, 
    0.5411439569827307, 0.5281019502265099, 0.5377906474095651, 0.5286362284777606, 0.5277745237636062, 
    0.5274479232024596, 0.5239404462226523, 0.5345155025399069, 0.5353175853652768, 0.5372270719473846, 
    0.5422316407718863, 0.5323805784039968, 0.556294985541241, 0.5349973642154522, 0.5343371978958091, 
    0.5318169179537702, 0.5336895448694923, 0.5415701940308547, 0.5433825111020142, 0.5453648457109866, 
    0.5502007875426553, 0.5379095584282799, 0.5293199520390408, 0.5456756669915886, 0.5332763873303475, 
    0.5383044041837883, 0.5421435396542256, 0.5411705128367228, 0.5366396561190369, 0.5376280085178357, 
    0.5469774301119814, 0.5363100241721458, 0.5455719326832164, 0.5357170570692277, 0.5385070831785769, 
    0.5320190265672421, 0.5287219237589696, 0.5376181459512138, 0.5404854271949074, 0.523344426298624, 
    0.5256502654154521, 0.5386777487017355, 0.5373857679675424, 0.5315486548559266, 0.5443318627646648, 
    0.5248858263883414, 0.5402467605617665, 0.531778074002026, 0.5421420946491602, 0.5477668819348802, 
    0.5435023480740561, 0.5279585949411846, 0.5333666897322775, 0.5402187413348739, 0.5394197158533645, 
    0.5363093927181231, 0.5380474564890748, 0.5362998901670949, 0.5412507800104698, 0.5261939773477781, 
    0.5317241036848269, 0.5330034627484047, 0.5488694594974258, 0.5459162111763637, 0.5357712120385801, 
    0.5382861732791917, 0.5329141550450577, 0.5525094877425138, 0.5371006420247575, 0.5421613899399235, 
    0.5415857897644535, 0.5372344265162957, 0.5484792864433286, 0.5402466586557837, 0.5336712456521826, 
    0.5414755647510866, 0.547028166946547, 0.5386560087905271, 0.5376686253695022, 0.5365390887581217, 
    0.5359888559228776, 0.5415032261984882, 0.5308809574020802, 0.5336510820643638, 0.5536953024527774, 
    0.5401402388173092, 0.539033580659154, 0.5372937701358587, 0.5429614431122798, 0.533211155863711, 
    0.5499722485419367, 0.5380547429788581, 0.5450752935842264, 0.5392586379608078, 0.5271758472699752, 
    0.5357456486609979, 0.538153380977793, 0.5349479001268281, 0.535370815097013, 0.5391504906474213, 
    0.5391170957198542, 0.5379750361969412, 0.5425244869663985, 0.5319919977702342, 0.53930693146023, 
    0.5368123898610474, 0.5338653806367178, 0.5371226364918606, 0.5419049020010239, 0.5349539592574919, 
    0.5398323126553131, 0.5453494351996113, 0.5448494676789764, 0.5405973902132009, 0.5393746705850181, 
    0.5337977806101036, 0.537989203786998, 0.53887600397202, 0.5336041497957432, 0.5380666954542328, 
    0.5441401604985139, 0.5442394486011661, 0.5384236174041926, 0.5372462771706232, 0.538011360114307, 
    0.5397291051802543, 0.5330198583441838, 0.5370348141045661, 0.5340401153971006, 0.5349975353286491, 
    0.540147982614659, 0.5376380509013111, 0.536901981750068, 0.5406809279399644, 0.5363113357202064, 
    0.5402399750842686, 0.538356553794751, 0.5380518662441407, 0.538733666876857, 0.538733666876857
]
y_ssim_ours = [
    0.5569800340652632, 0.5592900681966454, 0.5692328033758354, 0.5821276231088506, 0.5864529562232853, 
    0.5926903092906184, 0.6020995818046455, 0.5977061263302891, 0.6047105532780048, 0.6183386070920562, 
    0.6014552839187421, 0.6133924243070698, 0.6167668928283278, 0.6126752557673167, 0.6200100817938308, 
    0.6119478909433113, 0.6159289600992067, 0.6227212758426788, 0.6128071618249405, 0.6132851959639662, 
    0.6095726234319568, 0.6238715914054164, 0.6258587577702501, 0.6243180106066704, 0.6174359846215114, 
    0.6235885727087793, 0.6174187535475019, 0.6244423157947185, 0.6198263219969933, 0.6332907554893517, 
    0.6225942462334516, 0.6288089688322664, 0.6189435040027225, 0.6226120353787563, 0.6358372944499754, 
    0.6243349054556246, 0.6283348694732086, 0.6258712516592992, 0.6277791062223036, 0.6198132323533361, 
    0.6256994810056278, 0.634867879581306, 0.6342129217269864, 0.6346748914572442, 0.6347139034430314, 
    0.6328472793837803, 0.6262701705918703, 0.6281197210613737, 0.6293552920278026, 0.6305886201921066, 
    0.6260040421588174, 0.629413225921986, 0.637304960656727, 0.6289729464033339, 0.6266580792215756, 
    0.6299347248629771, 0.6397340072299804, 0.6254256240410141, 0.6338939987951756, 0.6348011454036263, 
    0.6276031425197092, 0.6402880735613656, 0.6311797870961908, 0.6345428073898888, 0.6336461004131955, 
    0.6352310559643835, 0.6324018773501898, 0.6332171220363102, 0.6354510944625874, 0.637854808007367, 
    0.6338547460534144, 0.6269954518978811, 0.6322894609695162, 0.6325075445736152, 0.6396357161765375, 
    0.6309746032102972, 0.6380887322286574, 0.6363100832540707, 0.6439717846989836, 0.6422130614707977, 
    0.6410335953661032, 0.6440866379122804, 0.6428697231960495, 0.6398579950581652, 0.6402616171735008, 
    0.6394635418024369, 0.6418183601799593, 0.6377159343500172, 0.6365495952709502, 0.6416200460686653, 
    0.6380498862226546, 0.6387893992294107, 0.6436579615237769, 0.6412476870057239, 0.6367800534239849, 
    0.6442461194561483, 0.6423168033442428
]

psnr_ = [20.671847130935056, 20.25255353910339, 20.295896907465195]
ssim_ = [0.6525140933249264, 0.6559652807234566, 0.6791030274063256]

x = range(1, len(y_ssim_ours)+1)
print(len(y_ssim_ours))
#x = [256, 512, 1024]

fig, ax = plt.subplots(1, 2)
ax[0].plot(x, y_psnr_ours)
ax[0].set_ylabel("PSNR")
ax[0].set_xlabel("Epochs")

ax[1].plot(x, y_ssim_ours)
ax[1].set_ylabel("SSIM")
ax[1].set_xlabel("Epochs")

plt.show()