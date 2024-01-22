#!/usr/bin/env python

#
# This script plots the empirical Uni v2 performance during 2023.
#

import os

import matplotlib.pyplot as pl
import numpy as np
from ing_theme_matplotlib import mpl_style

pl.rcParams["savefig.dpi"] = 200

POOL = os.getenv("POOL")
if POOL is None or len(POOL) == 0:
    POOL = "0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc" # v2 USDC/ETH
POOL = POOL.lower()

VERSION = 2

YEAR = os.getenv("YEAR")
if YEAR is None or len(YEAR) == 0:
    YEAR = "2023"

DAYS_PER_YEAR = 365

print(f"using pool {POOL} on Uniswap v{VERSION}, year {YEAR}")

# version 3 pool returns, computed by using the simulator
v3_005_fee_returns_2023 = [1.4425116788924157e-05, 2.463792810144448e-05, 1.6406561197362597e-05, 5.411937369140521e-05, 1.671148601758625e-05, 3.114584764213338e-05, 8.90442290133918e-06, 4.04997134799289e-05, 9.078622036684505e-05, 3.624089591138393e-05, 5.772348221367399e-05, 0.00014498952546371726, 0.0001338016467421065, 0.00021610907898547043, 8.52584691439911e-05, 0.00011984030020560253, 9.08935838794702e-05, 0.00019073436797563197, 7.027503495668402e-05, 0.00013586261002636942, 0.00013623085092628865, 9.562707832210101e-05, 0.00010000102219520952, 0.00012059355210289837, 0.00016188298874113445, 8.662778625025793e-05, 9.46340491235266e-05, 4.36655334369938e-05, 8.623693765081947e-05, 0.00010092730064365907, 7.994196796136032e-05, 0.0001298399441197787, 0.0001623437109679428, 8.129306477283138e-05, 4.6436006395489675e-05, 8.055549404570291e-05, 5.8756066583437594e-05, 8.65834223498998e-05, 8.808535663497868e-05, 0.0001446952074890226, 0.00011290457474169277, 4.012206293520115e-05, 3.894174786956673e-05, 0.0001551047945303232, 0.00012578066690455424, 0.00012082104019788148, 0.00018927665490459225, 0.00015120623321071162, 4.112676710478315e-05, 6.101663540911681e-05, 7.592830851586702e-05, 0.0001150151577309126, 0.00010088729761198729, 0.00010076514586534945, 0.00010985048824866231, 5.37872232829689e-05, 4.9772695698066386e-05, 6.515320508338134e-05, 5.985788512590725e-05, 7.109529360606306e-05, 5.862364526806583e-05, 9.932610298852307e-05, 2.435516490126769e-05, 4.275923188074767e-05, 3.9898102877039065e-05, 5.720985077504939e-05, 4.4788849637303566e-05, 0.00013797792040962475, 0.00040917882624430155, 0.0011509306533597824, 0.00040280667650603323, 0.000462436181174965, 0.0003681464854450024, 0.0002510921618818595, 8.629563610976302e-05, 0.00021238744486269792, 0.00016031894226563418, 0.00013055835715024725, 0.00013847143541812878, 0.0001129973578755497, 0.00017214274972265485, 0.00013920282576705575, 0.00011171229735814321, 4.287405507472843e-05, 4.672165543306105e-05, 8.539841465734282e-05, 7.006820727256278e-05, 6.45499374281239e-05, 7.152297844848121e-05, 5.5414735237307406e-05, 3.120916368358458e-05, 2.555147125240992e-05, 7.017709226560794e-05, 6.447909758584048e-05, 7.103374790755733e-05, 5.20490105693237e-05, 3.207288709416492e-05, 1.7161291033910906e-05, 3.2956595281901864e-05, 4.099232235960562e-05, 4.905327769180239e-05, 7.208923013704082e-05, 0.00011504532278654171, 0.00012617656279011302, 3.648715518889559e-05, 4.2619211181777055e-05, 5.011433794969876e-05, 4.5252795242146114e-05, 0.000112381225175622, 9.483672778673557e-05, 0.00010604206946688453, 2.9721708259363256e-05, 3.6716221695150877e-05, 7.326187152327983e-05, 6.376934298234479e-05, 0.00014454170431791452, 0.0001071603712775574, 4.510815113567268e-05, 2.2604187028868432e-05, 3.8753514063546654e-05, 7.946349948271538e-05, 5.747901298766052e-05, 6.826418962933769e-05, 4.617711136241544e-05, 0.00010120777366405882, 0.00011239907281219282, 5.196104034159987e-05, 8.804053310022445e-05, 4.537736029256546e-05, 7.583254054176281e-05, 9.093662374031924e-05, 9.740568426544047e-05, 3.759758797818708e-05, 2.6287715434726995e-05, 3.930044555948542e-05, 2.9808290196245577e-05, 3.723023418121417e-05, 3.2626079105300065e-05, 2.9896434942987205e-05, 1.4289095025081359e-05, 1.801329012631471e-05, 2.439996069421636e-05, 3.139851291717868e-05, 4.222357760418615e-05, 3.625334061814316e-05, 2.8794991281868492e-05, 1.388134354557661e-05, 5.206762859963986e-05, 4.2665220629452274e-05, 3.272973992400576e-05, 3.310134451676922e-05, 3.621688822246302e-05, 3.24476202368311e-05, 1.0876200715085835e-05, 1.4042374924011927e-05, 7.046491189486663e-05, 5.488371255581864e-05, 5.065620382369962e-05, 2.0883176463469606e-05, 1.9294823944581232e-05, 0.00014033261840121675, 3.299303639090687e-05, 5.666880198842319e-05, 4.657151916942164e-05, 8.524574576164702e-05, 9.592351018705536e-05, 5.6159802775634625e-05, 3.095048394282886e-05, 2.2202705636671438e-05, 5.046683428726885e-05, 6.251947040228065e-05, 0.00010492361202230958, 5.6815970589893136e-05, 5.6361031089320135e-05, 2.5063008865414778e-05, 3.594849541178066e-05, 6.593220321048498e-05, 4.174567800194079e-05, 4.8078395978295586e-05, 3.913811554283221e-05, 0.0001006936084805988, 2.6984386281387307e-05, 2.7823442752191085e-05, 3.986496241243667e-05, 2.4747827737300735e-05, 3.614425855414031e-05, 5.390470890473903e-05, 3.5483922445016834e-05, 1.6321444799017282e-05, 1.7955749514007435e-05, 2.9509744607182643e-05, 2.314579871556623e-05, 3.121951936453888e-05, 7.841655321991023e-05, 6.492072832853906e-05, 2.0416991202235225e-05, 1.7741070240056425e-05, 4.0373136994803476e-05, 3.078515469273236e-05, 2.8758215152897876e-05, 3.128179433105527e-05, 1.62369829742253e-05, 1.878666928236108e-05, 1.626366789109861e-05, 3.7782692193903946e-05, 1.6790764263155884e-05, 3.374343479672073e-05, 2.1689510678430704e-05, 1.1588839462317415e-05, 6.754279275194007e-06, 1.9834480711232763e-05, 2.2160897953430384e-05, 3.849901905206043e-05, 3.0011537855767924e-05, 1.978939321325714e-05, 2.1871406818731755e-05, 5.892348526903929e-06, 8.928048053242446e-06, 2.5791116234450786e-05, 2.776051549061497e-05, 2.065425981228983e-05, 1.3030584330157108e-05, 8.946311554301249e-06, 3.443031678544904e-06, 6.50589644458182e-06, 9.981834457899197e-06, 1.361991167933958e-05, 1.804124974023892e-05, 0.00024936783977935555, 0.00012359686932536293, 3.776460490233497e-05, 2.505500721479909e-05, 3.120425676000198e-05, 7.914634969649796e-05, 5.0529175312544514e-05, 2.9398712742954922e-05, 3.690061634180281e-05, 6.199955118816372e-06, 1.2125192532038335e-05, 2.8510634911289508e-05, 7.270304563537625e-05, 2.9328115132060733e-05, 5.7436160085898006e-05, 5.551267180809583e-05, 1.2072885643923596e-05, 1.439898038184156e-05, 2.337300607138045e-05, 2.676279261832572e-05, 2.5183387009895786e-05, 2.1122371698359522e-05, 2.0235245135243107e-05, 3.3290374389431e-06, 2.597395990903013e-05, 0.0001455452761568539, 5.898487541139847e-05, 4.98895010278559e-05, 3.8457103810951807e-05, 2.702985544004424e-05, 1.1836996349923577e-05, 1.1884337019375647e-05, 4.43648881439861e-05, 3.776512928522199e-05, 2.9905517745762098e-05, 3.750669156421307e-05, 2.1516106033390915e-05, 7.554458666840213e-06, 1.4143471192417034e-05, 3.5261280561692246e-05, 1.9645333846082526e-05, 3.08335985181161e-05, 5.2978229695308245e-05, 4.196964425827039e-05, 1.6317608963370303e-05, 3.626617497238111e-05, 8.993248710584078e-05, 3.236218292815946e-05, 3.645609049590682e-05, 3.185780548279746e-05, 4.0702923836067234e-05, 9.537401390090262e-06, 2.8767220786179962e-05, 5.2718965564470114e-05, 3.8301099184367714e-05, 4.50874424593111e-05, 3.870350115668115e-05, 2.9455373265520996e-05, 9.999340757766937e-06, 1.54693181758364e-05, 8.447808523224443e-05, 3.9496265425302216e-05, 4.938573270975525e-05, 2.8858383434536523e-05, 5.5153916452150074e-05, 3.1664896276961205e-05, 3.678675091284087e-05, 0.00013506672634670287, 0.00021967545251706783, 8.998193717458444e-05, 0.00010732451603646348, 5.658229434488259e-05, 2.1204740095100912e-05, 2.580849583065746e-05, 5.0626484346768814e-05, 4.783296071279646e-05, 7.745360492391285e-05, 7.345518980137193e-05, 5.8149753807606716e-05, 2.9108425402676714e-05, 6.99399387080416e-05, 6.562493643046309e-05, 5.628869196570947e-05, 3.296242916105496e-05, 0.000203949652966823, 0.00010770294091420795, 7.415268926687181e-05, 4.984495103156796e-05, 0.00010005118924758353, 0.00010273828502509553, 7.964958363013362e-05, 0.00010973467651260747, 9.203326187371562e-05, 4.880634569757361e-05, 3.6736460159778786e-05, 7.136973591203392e-05, 9.317746156460321e-05, 8.692268639454596e-05, 3.947962081882364e-05, 6.12393588883775e-05, 1.765344214331833e-05, 3.456294794889839e-05, 5.3243930178367956e-05, 5.3099609161567774e-05, 4.383989984473745e-05, 3.244618371843984e-05, 4.818132763629471e-05, 5.07967503319456e-05, 4.486602467862932e-05, 0.00016445518770093524, 0.00012455663733629746, 9.146771582077761e-05, 9.901563428688537e-05, 6.861823422276305e-05, 7.182748411552373e-05, 3.212082695043432e-05, 0.00015435763840780724, 8.706560583278144e-05, 0.00011057127681628158, 7.699510467631863e-05, 6.853903269040326e-05, 0.00012856855576606036, 5.519155420577768e-05, 7.630224733678349e-05, 6.698345314153775e-05, 0.00010032878782543552, 8.796938275744745e-05, 0.00010309590328468735, 4.592668410784936e-05, 5.412967997520413e-05, 4.054275644233918e-05, 6.545119756720403e-05, 9.307044327193042e-05, 0.00019818010293403334, 9.645857887087965e-05, 4.1878610060017275e-05, 4.8930790486770904e-05]


v3_03_fee_returns_2023 = [6.7916548061616294e-06, 2.43351230547262e-05, 7.333207767602909e-06, 7.153861715873699e-05, 1.3216582635124407e-05, 3.0946721492690914e-05, 5.149054900120718e-06, 2.7502826791308074e-05, 6.774200786068301e-05, 3.431896229366639e-05, 6.21782647647144e-05, 0.00014227137112627584, 7.03103102606733e-05, 0.0002524505779555719, 9.439721684195213e-05, 0.00013910593082508508, 0.00011686963838391564, 0.00021970006891379167, 5.992445920476135e-05, 8.12396672689637e-05, 0.0001306970741732567, 9.123671257365607e-05, 0.00011415424788982749, 9.363956852741478e-05, 0.00021494057863035, 7.682658876192315e-05, 9.709696174791179e-05, 3.353383048804492e-05, 9.967684121587921e-05, 0.0001070022167247647, 6.08002528979225e-05, 0.00010562217302357973, 0.00016150062461823197, 9.584352185239903e-05, 4.409009234743504e-05, 5.201193251640267e-05, 7.24363070710315e-05, 8.449998814395241e-05, 6.497251771931631e-05, 0.00016564041657045938, 0.0001231553032189892, 2.99448925020447e-05, 4.3876650713525074e-05, 0.00015246620310871753, 0.0001285826816739392, 0.00010933382578054006, 0.00021204221396783213, 0.00012522785953469957, 2.2241374418952e-05, 6.303626765294988e-05, 7.447152182403438e-05, 0.00010554249406060134, 0.00010283628992688785, 0.00010534292978032013, 9.183197920203309e-05, 3.9665743825936494e-05, 5.8418169327636916e-05, 5.743811560862279e-05, 4.8566237631084246e-05, 7.775944958433001e-05, 4.4896461774487875e-05, 0.00013066855199894215, 1.8244829779835555e-05, 4.3657763473398935e-05, 2.4846715641671427e-05, 6.682814154781666e-05, 4.620481580969736e-05, 0.0001449746027910657, 0.0003524253887034523, 0.0009351042805796206, 0.0003191345613619658, 0.00024907684510641046, 0.0002903752348573037, 0.00022029225286990007, 9.538986600748774e-05, 0.0001894073354564669, 0.00017651842690266818, 0.00013120241721210126, 0.0001462054121277231, 0.00012638165528345888, 0.00018339355617104326, 0.00010416609266118107, 0.0001282342140856686, 4.236022794587092e-05, 5.745174610291624e-05, 8.946946597900726e-05, 8.680321001503663e-05, 5.578964348218564e-05, 8.708813926627568e-05, 5.792251326223452e-05, 4.182740331952769e-05, 3.400397233556308e-05, 0.00011146931074604871, 6.823509966355798e-05, 7.843570642218173e-05, 6.27737389829823e-05, 2.6206767810555915e-05, 1.5656555385282327e-05, 3.4508455619385545e-05, 4.8909567198466494e-05, 4.405734197612387e-05, 8.767253295968151e-05, 8.26135804608455e-05, 0.0001437040460297432, 3.3399013753618385e-05, 5.6475583103913675e-05, 4.760929580140857e-05, 5.173725035297553e-05, 0.00013289399267397232, 0.00010201287093805636, 0.0001303445717168384, 2.882717447007101e-05, 4.494675853416305e-05, 0.00010155452598495119, 6.365395650231538e-05, 0.00019548660409837316, 0.00014977854227348188, 4.0274685176013516e-05, 2.0772532562675153e-05, 5.604122753625076e-05, 6.830221699243591e-05, 4.239341493340413e-05, 8.688975123369752e-05, 2.8612930678536373e-05, 8.8999864982048e-05, 0.0001139879262017777, 6.451794196997242e-05, 9.681581648746507e-05, 3.535336255957389e-05, 0.00010450409941359974, 8.23748109066147e-05, 0.00014007057875563953, 2.598767126016258e-05, 2.0103878582545682e-05, 4.5989792781225205e-05, 2.702313008127824e-05, 3.792686402439977e-05, 4.3512510571233424e-05, 2.391497476047132e-05, 8.409962770746936e-06, 1.0541743209668083e-05, 1.8213425667538842e-05, 3.046497118085318e-05, 3.852052986260332e-05, 3.9774158770859655e-05, 2.5474330744249375e-05, 7.61410008313718e-06, 5.3855423270657204e-05, 4.03323079287841e-05, 2.8207431628121505e-05, 3.0325563199198292e-05, 3.9695178756557915e-05, 3.425631536464193e-05, 8.304516094200627e-06, 1.7464523679130358e-05, 7.426614780481443e-05, 6.253760530551527e-05, 6.050140515609391e-05, 1.7938447694055022e-05, 1.9856023897131816e-05, 0.0001234644161411268, 3.328680720842073e-05, 4.814271593279971e-05, 4.304489862603803e-05, 8.149815927729422e-05, 5.862052538621284e-05, 4.6707044409880875e-05, 3.415330571570751e-05, 1.949214296626974e-05, 5.458418892121498e-05, 6.474506526806326e-05, 0.00011402964791579037, 7.067697064935665e-05, 7.469513404324176e-05, 2.991854096583711e-05, 4.2545588301555115e-05, 7.854879808348032e-05, 4.549903506102354e-05, 4.401800907793943e-05, 3.5404408613721094e-05, 0.0001389050114363728, 1.308105692575026e-05, 5.7193383008634024e-05, 3.593592777152961e-05, 1.5930370022956572e-05, 2.769703382541786e-05, 7.636402821996226e-05, 3.3779892598507514e-05, 1.5816643785396692e-05, 1.4369866839075125e-05, 4.003796603926031e-05, 1.6458776556515056e-05, 2.6099667458305153e-05, 0.0001017575760951222, 7.952992014292267e-05, 8.579209400982585e-06, 1.679020227675668e-05, 6.162267459514468e-05, 2.7426490289990723e-05, 3.165733590809755e-05, 3.3573359550693294e-05, 1.0996611586553686e-05, 2.3970709984488524e-05, 2.3260389893910446e-05, 2.941722430840869e-05, 8.33574317000969e-06, 2.793514846584059e-05, 1.3448826806303126e-05, 1.1482441671758287e-05, 3.2960471198783077e-06, 1.229722198162047e-05, 1.0548811730042786e-05, 4.128615476598556e-05, 3.141626070884795e-05, 1.824454454650432e-05, 1.462128918290367e-05, 3.1270157708380973e-06, 1.113469746791437e-06, 2.5436930669031232e-05, 2.9207744745929755e-05, 9.36720427570844e-06, 9.191969378678232e-06, 4.510304365730067e-06, 1.245087036272713e-06, 8.834147311810098e-06, 6.664721541001966e-06, 1.214606608805878e-05, 1.2624438096675493e-05, 0.0005551101258602881, 0.00011369905177276259, 3.197286611056555e-05, 1.8772848532375107e-05, 3.59542330680105e-05, 8.983703479997081e-05, 6.909508237520217e-05, 2.5780156139008048e-05, 4.3907758345129305e-05, 3.056927638554563e-06, 4.174410970240532e-06, 3.381544572494866e-05, 8.619629019411575e-05, 2.0063199516002892e-05, 6.8698492342685e-05, 4.615660671902992e-05, 7.89254689640362e-06, 9.53143276379898e-06, 1.9888321622310727e-05, 2.8498398349916093e-05, 4.414340281287533e-05, 2.204370936723502e-05, 2.3333628205818126e-05, 2.441596340961492e-07, 2.3502255170323036e-05, 0.00011538848704538586, 8.686966161127634e-05, 5.091334452203292e-05, 3.904581271143963e-05, 2.7852554114821007e-05, 6.488560622950247e-06, 1.3997709697827227e-05, 4.393814011959071e-05, 3.543442049399821e-05, 3.213087988302411e-05, 3.4384646895651495e-05, 1.3735615422585908e-05, 1.2615329292426688e-06, 1.7030948895990758e-05, 3.084232549629957e-05, 1.1411101411734733e-05, 4.2124240669366684e-05, 6.227580206473107e-05, 4.6141675553699695e-05, 1.7525413022587345e-05, 4.363969875304255e-05, 0.00011216368837469116, 1.8601338956834914e-05, 3.676302247334114e-05, 2.6410775024292207e-05, 4.7742787095163e-05, 5.929276942550677e-06, 4.163785826800521e-05, 6.132483650424503e-05, 3.554578853542744e-05, 4.253798850370346e-05, 3.8156121277369087e-05, 3.353685716955051e-05, 5.722310817185247e-06, 9.224869069778778e-06, 0.00013385158134928513, 4.279888033893306e-05, 2.689161107465938e-05, 2.4550788870101343e-05, 5.5609031330979426e-05, 2.8142281632280504e-05, 4.038041241769443e-05, 0.0001749776719839256, 0.00021320724314660225, 7.357761257067267e-05, 0.00014234590446914766, 6.0463999521167344e-05, 2.386431576787579e-05, 3.0024498155584277e-05, 6.0881245057205304e-05, 4.509054293361369e-05, 9.779149207553631e-05, 6.762873191566543e-05, 4.879403296705713e-05, 2.312576002253967e-05, 9.122800713934902e-05, 5.321486802259817e-05, 5.1716739963358305e-05, 1.812347119765384e-05, 0.00027577516816964474, 0.0001082159585169121, 6.540768379572185e-05, 4.790075836048029e-05, 0.00014189044884092014, 0.00012640403649652197, 9.170979869545726e-05, 0.00014287942627591948, 8.343529317336054e-05, 3.581987644447428e-05, 3.361846078499016e-05, 9.423431709382532e-05, 0.0001302139925454716, 0.00010312058724835727, 4.4305004884424256e-05, 6.829169606404255e-05, 1.0783146263575031e-05, 4.049104860860434e-05, 6.271219266515963e-05, 5.4890625741791646e-05, 3.59003360491937e-05, 2.5983021938355055e-05, 4.7535099866316305e-05, 6.23175664779092e-05, 3.7754672101584725e-05, 0.00013239542180653392, 0.00011651918022695214, 8.478525327752967e-05, 0.00010961730933192503, 5.708181167334533e-05, 9.17857176953108e-05, 3.0120254983195744e-05, 0.00016741189768443933, 7.608342889173746e-05, 0.000159786984937952, 8.85584085752562e-05, 6.756842111972274e-05, 3.7106719443980377e-05, 5.0045854386662337e-05, 8.423185302677449e-05, 8.51411581294024e-05, 0.00016310507606002292, 8.969112673216666e-05, 0.0001281587970821253, 3.820988893210231e-05, 5.0565330841860955e-05, 3.888859151088913e-05, 6.721845373349982e-05, 7.862793392046066e-05, 0.00018994145647079427, 0.00011668612801014085, 4.046815277772819e-05, 4.960042146787836e-05]

v3_10_fee_returns_2023 = [0.0, 3.275564969770938e-05, 3.095679670175491e-08, 9.491406483234382e-05, 4.187014827536578e-06, 4.164846812237255e-05, 0.0, 3.2891188254569676e-05, 0.00010096315616634455, 3.926773838953765e-06, 8.970683455044623e-05, 0.00014913639946282002, 7.366225764782252e-05, 0.00030593439478885786, 4.364996268664292e-05, 0.00014532416258687317, 0.0001015244509860672, 0.0004422706214465093, 6.947808230755972e-05, 0.00015071039930917855, 0.00010241930600528041, 9.105426506096791e-05, 5.603189537500243e-05, 0.00010245825384198319, 0.00026763889064659017, 3.3647414492540576e-05, 9.490949497495243e-05, 4.58151690719254e-05, 0.00011519686157712063, 0.0001362183221125038, 6.210365981209843e-05, 9.389324939621148e-05, 0.00021266134138582535, 3.0008582243379942e-05, 2.3291389788961553e-05, 7.327839063704995e-05, 5.7405689612364544e-05, 0.00011986542328918118, 9.445976988114698e-05, 0.000170604725310249, 5.4604266500552265e-05, 2.8611324824669327e-05, 3.425982187231389e-05, 9.15181869495292e-05, 9.132841449215462e-05, 0.00016717551809324478, 0.00026609334268780854, 9.468569519531565e-05, 1.2372482590745778e-05, 3.717397144224892e-05, 7.286616130687289e-05, 6.69910692816274e-05, 8.331246843783508e-05, 7.921704639616467e-05, 9.499323544772972e-05, 5.520709646722306e-05, 0.0001010494142469225, 3.449444993487254e-05, 6.916513464772574e-05, 9.718460947525252e-05, 6.367877657520457e-05, 0.00011997438275616797, 0.0, 9.578860702450831e-06, 1.7963417182602967e-07, 4.137938389665666e-05, 2.7209365300532357e-05, 0.00018253749028388272, 0.00025665556820515616, 0.0034869445598027637, 0.0001911462402052855, 0.00015983705168326918, 0.0002739313861611692, 0.00015101819657423163, 3.2045021842662494e-05, 0.00022117842583595676, 0.00012875072891792706, 0.00010697710015820625, 0.0001658382121438297, 0.00013129809585103505, 9.228859873376451e-05, 0.00020514649410819307, 0.00010743423738752987, 1.8404369042182933e-05, 5.87697853047989e-05, 0.00012959467315470333, 8.799836364058416e-05, 3.9241386454992586e-05, 4.620133416674669e-05, 7.548755697741691e-05, 2.9616665329414395e-06, 5.087100362617598e-05, 0.00011318381312399024, 9.157013187260412e-05, 9.994108922724309e-05, 4.164445773651579e-05, 1.0780016861436721e-05, 0.0, 3.1965059646102385e-05, 6.0527749156319186e-05, 0.00010301979200888657, 0.00014183306022094662, 0.00011320402003276685, 0.0002154898143473349, 0.0, 2.4805687543226654e-05, 3.8480469196038166e-05, 4.691366098978494e-05, 0.00018273705579028413, 4.947682742808108e-05, 0.00012341141897803098, 2.313207079566564e-05, 1.5795686950625284e-05, 7.636697946075987e-05, 5.805120735222701e-05, 0.0003375934982997248, 0.000159876193657006, 2.2929469561917974e-05, 0.0, 6.09541807413537e-05, 9.05460045814046e-05, 3.901285549787868e-05, 0.0001731983550231366, 4.650198996178863e-05, 0.000118554241824449, 0.0002636770760768134, 4.976959018627926e-05, 7.85414139469763e-05, 1.4764223200850133e-05, 0.00014407327580858248, 7.203379740867026e-05, 0.0001074678550597295, 1.477721925580632e-06, 1.0290322314440184e-05, 3.217576010940033e-05, 1.862769542914513e-05, 4.234449826136252e-05, 4.875028641801817e-05, 1.1447466501541571e-05, 0.0, 0.0, 0.0, 5.5418994452156354e-05, 6.779851910260745e-05, 4.709808104034254e-05, 3.421403502995597e-05, 4.0958861353059933e-07, 0.00010080316986409464, 2.8212047956556004e-05, 2.2987546565757107e-06, 3.781339305001251e-05, 8.024372532670434e-06, 3.728793520202562e-05, 6.700139955881535e-07, 4.906743876341797e-06, 0.00012390126575980258, 0.00010175253481076913, 5.029078986087058e-05, 0.0, 0.0, 0.00016952818333931837, 8.551711443275638e-06, 2.8781612166481333e-05, 1.1843478229412037e-05, 0.00014681972179994885, 3.894884332283592e-05, 6.859668499953183e-05, 5.864190427428048e-05, 6.202094208234203e-06, 4.212740940344864e-05, 7.937069433955656e-05, 0.00014081712247048184, 8.119232526339776e-05, 6.509297222722328e-05, 2.0520047917041943e-05, 4.313512519846158e-05, 5.8085965711427855e-05, 4.380387863563238e-05, 7.044775714410598e-05, 2.945916191070558e-05, 0.00018597674165606363, 0.0, 5.822470238000728e-05, 2.3072353492827297e-05, 4.053369001115269e-06, 4.863595018507905e-05, 0.00012365292794422545, 2.8737069020322297e-05, 3.6460967859341005e-06, 5.396534748139696e-06, 3.601812299047119e-05, 0.0, 0.0, 0.0001385917895506345, 0.00012954965652083592, 7.152041115981365e-06, 6.444690990975016e-12, 5.382826712435638e-05, 4.643787781394556e-06, 7.077844425465121e-06, 2.2338693811238434e-05, 3.032180974410365e-10, 3.392092114841444e-05, 1.512135021058315e-05, 4.036995567477245e-05, 0.0, 1.893077252339662e-05, 1.5944208912435767e-09, 0.0, 0.0, 8.249576180818223e-07, 1.2315733343857988e-07, 7.951311371544693e-05, 3.311931827017355e-05, 0.0, 9.10843227223105e-06, 2.329376260459933e-07, 0.0, 1.6630235743132767e-05, 4.548765007478171e-05, 2.1377223805627236e-08, 0.0, 0.0, 5.426278591403587e-06, 0.0, 2.3359687312441514e-08, 2.5005425306221256e-05, 2.2827287439300372e-05, 0.0005989973625451464, 5.1567193075798435e-05, 2.7787986464175648e-05, 0.0, 8.889271276263535e-06, 0.00014065903383524885, 0.00010499607718012611, 3.1275481319100287e-05, 9.401714667017966e-06, 0.0, 0.0, 1.1873833483172682e-05, 0.00011590015040672893, 1.2435053909279051e-05, 9.34644990429462e-05, 4.965608912558676e-05, 1.2754737301252085e-05, 4.716891297133092e-09, 7.202677708168262e-06, 7.366210969919379e-06, 6.409931182294614e-05, 1.709297980414509e-06, 1.156796902921638e-05, 0.0, 2.5747712676728564e-05, 0.00010054293741399436, 9.442477302996475e-05, 7.182265167817678e-06, 3.554700577990022e-05, 2.0809672659480298e-05, 0.0, 8.518317640226835e-06, 4.943156109189921e-05, 7.173139270404079e-06, 3.461878076596008e-05, 5.3601090900834214e-05, 1.8340221906328203e-07, 9.520730990098209e-07, 4.6441737687674926e-11, 1.53116615506677e-05, 0.0, 8.928293901027396e-05, 9.324303236038626e-05, 2.0574780283823634e-05, 1.074885352714241e-05, 5.9914351294181396e-05, 0.00011524830362645718, 7.039868306169077e-07, 1.1636050497308597e-05, 3.070537488232893e-05, 2.8606010275334454e-05, 0.0, 2.2491780084818988e-05, 0.0001088611356856555, 2.999971725636951e-05, 7.1997890774504955e-06, 4.427666825007352e-05, 3.200823722866445e-05, 2.917030433657919e-08, 0.0, 0.00014374983085294605, 3.242384426059263e-05, 1.4717134178944943e-13, 3.207390733347223e-05, 8.703699904993753e-05, 3.2982057781037107e-05, 3.66001950132929e-05, 0.00025095474436152723, 0.00018870856469284446, 4.426217598309831e-05, 0.00017603932782005372, 2.8474198738466346e-05, 1.551737215743479e-05, 1.833058003916301e-05, 2.6240516706612463e-05, 0.0, 6.808344989366882e-05, 9.010907623174015e-05, 6.363644291134429e-05, 4.8495423282903766e-05, 7.812131131429999e-05, 5.144932281106756e-06, 4.869492089129839e-05, 0.0, 0.00027287890576840185, 3.230046203229957e-05, 6.365161817297008e-05, 4.073274764944962e-05, 8.166058397068462e-05, 0.00012720119279877121, 8.473418015526272e-05, 0.00017430834506413005, 7.616079207006283e-05, 1.1434330494799919e-05, 5.2331098549972e-05, 7.386728009610991e-05, 0.00017543574024474936, 0.0001405273457547429, 2.5917336402696307e-06, 7.630436910043922e-05, 0.0, 3.4024919070554564e-05, 6.834101477177674e-05, 5.429725994977073e-05, 1.5294975060193875e-05, 0.0, 5.805159369945054e-05, 8.970369835512428e-05, 2.916155872746157e-05, 9.382273156063215e-05, 0.00012019206045538362, 4.121318915403549e-05, 0.00011405589372425295, 2.285472589053743e-05, 4.254021383873097e-05, 1.6985402597247228e-05, 0.00021683075302263315, 5.5530001556392214e-05, 0.0001162992194244722, 0.0001303138978695902, 8.368631599140513e-05, 0.0, 1.9535248317927668e-05, 0.00016518245299240774, 0.00011379894209248155, 0.0001512400752982095, 0.00014339728046200163, 8.499574372925599e-05, 2.5360272741442476e-05, 4.3466210362735674e-05, 8.009824266285606e-06, 8.559936542603891e-05, 0.0001708356935843597, 0.0001220175542145191, 0.0001203955345706255, 1.4727381590101202e-05, 1.4758524940451247e-05]


self_dir = os.path.dirname(os.path.abspath(__file__))

def load_csv(filename):
    result = []
    with open(os.path.join(self_dir, filename)) as f:
        for line in f.readlines():
            fields = line.strip().split(",")
            if len(fields) == 0:
                continue
            result.append([float(u) for u in fields])
    return result


def hodl(price, price_0):
    return price_0 / 2 + price / 2


def calculate_daily_vols(prices, period):
    log_returns = []
    for i in range(len(prices) - 1):
        log_returns.append(np.log(prices[i] / prices[i+1]))

    PERIOD = 7
    vols = []
    for i in range(2, period):
        sd = np.std(log_returns[0:i])
        vols.append(sd)

    for i in range(len(prices) - (period - 1)):
        sd = np.std(log_returns[i:i+period])
        vols.append(sd)
    return vols

#
# Fee return for a day is the difference between the actual share value at the end
# of the day vs. the 
#
def get_fee_return(i, share_values, eth_prices):
    p_0 = eth_prices[i]
    p_1 = eth_prices[i+1]
    v_0 = share_values[i]
    v_1 = share_values[i+1]
    v_expected = v_0 * np.sqrt(p_1 / p_0)
    return (v_1 - v_expected) / v_1


def avg_filter(array, period):
    result = []
    for i in range(1, period+1):
        result.append(np.mean(array[0:i]))
    for i in range(len(array) - period):
        result.append(np.mean(array[i:i+period]))
    return result


def main():
    mpl_style(True)

    filename = f"reserves-v{VERSION}-{YEAR}-{POOL}.csv"
    data = load_csv(filename)
    n = len(data)
    x = range(1, n + 1)

    pl.figure(figsize=(6, 4))

    share_values = [data[u][-2] for u in range(n)]
    share_0 = share_values[0]
    eth_prices = [data[u][-1] for u in range(n)]
    price_0 = eth_prices[0]

    pl.plot(x, [100 * u / share_0 for u in share_values], label="LP")
    pl.plot(x, [100 * hodl(price, price_0) / price_0 for price in eth_prices], label="HODL 50:50")
    pl.plot(x, [100 * price / price_0 for price in eth_prices], label="ETH")

    pl.ylabel("Relative value, %")
    pl.xlabel("Day in 2023")
    pl.legend()
    pl.savefig("2023-price-and-pnl.png", bbox_inches='tight')
    pl.close()


    pl.figure(figsize=(6, 4))

    lp_returns = [u / share_0 for u in share_values]
    hodl_returns = [hodl(price, price_0) / price_0 for price in eth_prices]
    
    pl.plot(x, [100 * (a - b) for a, b in zip(lp_returns, hodl_returns)], label="Relative LP returns")
    pl.ylabel("PnL over HODL, %")
    pl.xlabel("Day in 2023")
    pl.legend()
    #pl.show()
    pl.savefig("2023-pnl-over-hodl.png", bbox_inches='tight')
    pl.close()


    pl.figure(figsize=(6, 4))

    period = 7
    vols = calculate_daily_vols(eth_prices, period)
    lvr = [100 * (sigma ** 2) / 8 for sigma in vols]
    lvr_30 = [100 * (sigma ** 2) / 8 for sigma in calculate_daily_vols(eth_prices, 30)]
    lvr_100 = [100 * (sigma ** 2) / 8 for sigma in calculate_daily_vols(eth_prices, 100)]

    fee_returns = [100 * get_fee_return(i, share_values, eth_prices) for i in range(len(eth_prices) - 1)]
    fee_returns = avg_filter(fee_returns, period)

    v3_005 = avg_filter([100 * u for u in v3_005_fee_returns_2023], period)[:-1]
    v3_03 = avg_filter([100 * u for u in v3_03_fee_returns_2023], period)[:-1]
    v3_10 = avg_filter([100 * u for u in v3_10_fee_returns_2023], period)[:-1]

    x = range(1, n)
    pl.plot(x, fee_returns, label=f"v2 fee returns ({period} day avg)")
    pl.plot(x, lvr, label=f"LVR ({period} day avg)", color="red")
    pl.ylabel("Daily LVR and fees, %")
    pl.xlabel("Day in 2023")
    pl.legend()
    #pl.show()
    pl.savefig("2023-fee-returns-v2.png", bbox_inches='tight')
    pl.close()


    if POOL != "0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc":
        return


    pl.figure(figsize=(6, 4))
    period = 30
    vols = calculate_daily_vols(eth_prices, period)
    lvr = [100 * (sigma ** 2) / 8 for sigma in vols]
    lvr_30 = [100 * (sigma ** 2) / 8 for sigma in calculate_daily_vols(eth_prices, 30)]
    lvr_100 = [100 * (sigma ** 2) / 8 for sigma in calculate_daily_vols(eth_prices, 100)]

    fee_returns = [100 * get_fee_return(i, share_values, eth_prices) for i in range(len(eth_prices) - 1)]
    fee_returns = avg_filter(fee_returns, period)

    v3_005 = avg_filter([100 * u for u in v3_005_fee_returns_2023], period)[:-1]
    v3_03 = avg_filter([100 * u for u in v3_03_fee_returns_2023], period)[:-1]
    v3_10 = avg_filter([100 * u for u in v3_10_fee_returns_2023], period)[:-1]

    x = range(1, n)
    pl.plot(x, fee_returns, label=f"v2 fee returns ({period} day avg)")
    pl.plot(x, v3_005, label=f"v3 0.05% fee returns ({period} day avg)")
    pl.plot(x, v3_03, label=f"v3 0.3% fee returns ({period} day avg)")
    pl.plot(x, v3_10, label=f"v3 1.0% fee returns ({period} day avg)")
    pl.plot(x, lvr, label=f"LVR ({period} day avg)", color="red")
    #pl.plot(x, lvr_30, label="LVR (30 day avg)", color="brown")
    #pl.plot(x, lvr_100, label="LVR (100 day avg)", color="yellow")
    pl.ylabel("Daily LVR and fees, %")
    pl.xlabel("Day in 2023")
    pl.legend()
    #pl.show()
    pl.savefig("2023-fee-returns-v2-vs-v3.png", bbox_inches='tight')
    pl.close()


if __name__ == "__main__":
    main()
