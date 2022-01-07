import include_parent_path
from matplotlib import pyplot as plt

loss = [
    2.7724635889053344, 2.2072355926513674, 2.096526228427887, 2.06140885515213, 2.016094368648529, 
    2.0021075924873353, 1.9935115487098694, 1.9863678719520568, 1.981664315891266, 1.9781543600082399, 
    1.974095228290558, 1.9698838570594788, 1.9668965879440308, 1.9641724520683288, 1.9599792243003846, 
    1.9559344895362853, 1.9541016772270203, 1.948895700931549, 1.9471769709587097, 1.9455449079036713, 
    1.9426551619529724, 1.9394354032039642, 1.9368604166030883, 1.933595255947113, 1.933083219432831, 
    1.9302157666683197, 1.9277581301689148, 1.9257099493980407, 1.9248478688240052, 1.9216482118606568, 
    1.9201052247047425, 1.9188665002822876, 1.918711414718628, 1.918378714942932, 1.91505022482872, 
    1.915043951320648, 1.9128304371833802, 1.9116137744903565, 1.9106066952705383, 1.9087219751358033, 
    1.9086492548942566, 1.908967088985443, 1.906520496749878, 1.9051436264038086, 1.9024888896465302, 
    1.9013239415168761, 1.8981974615097046, 1.8967976773262023, 1.8974193707466125, 1.8955796638488769, 
    1.8939100205421449, 1.8921825117588043, 1.8921208405017853, 1.8906136825561524, 1.8908314285755157, 
    1.8890468599319459, 1.8872761236190796, 1.887644455909729, 1.885704342842102, 1.88614166264534, 
    1.8861527401447296, 1.8837461201667787, 1.8850234541893005, 1.8832795888423919, 1.883663484477997, 
    1.8830505338191985, 1.8807997732162476, 1.8818903357982635, 1.8794559719562531, 1.880171683883667, 
    1.879997449207306, 1.8782558438301087, 1.878446954059601, 1.8774945796966553, 1.8770291977882385, 
    1.8760377758979798, 1.8744973860740661, 1.8746416621685027, 1.875662728023529, 1.8745009472846985, 
    1.874043968296051, 1.8729411910057068, 1.8737784202575685, 1.8713531993865966, 1.8709013212680816, 
    1.8699909198760987, 1.870860435962677, 1.873238758945465, 1.8700430693626404, 1.8712958879470825, 
    1.8693078245162964, 1.8688264626979827, 1.86877231092453, 1.8687719528198241, 1.8682122053146362, 
    1.8675712918281555, 1.8673015007495881, 1.866410393333435, 1.867264084339142, 1.865641745376587, 
    1.8659913820266725, 1.8639113955497741, 1.8655491475105286, 1.863427071905136, 1.8616578248023987, 
    1.859100241136551, 1.8601711097717286, 1.8601791062355042, 1.8589258175373078, 1.8588486088752747, 
    1.8582036061286926, 1.857608585166931, 1.8567905312538147, 1.855588622188568, 1.8560214447021484, 
    1.8535368832588195, 1.8535897209644319, 1.8520419958114624, 1.8518920823574065, 1.8522481996536255, 
    1.851048882007599, 1.851728453350067, 1.8497891535758972, 1.8499245536327362, 1.849069253396988, 
    1.8485504848003387, 1.8465232748031617, 1.847928059387207, 1.846468802690506, 1.8462307916641236, 
    1.8465689796924591, 1.845043642807007, 1.8451828238487245, 1.846105673122406, 1.8436509612083436, 
    1.8438509731292725, 1.84318679895401, 1.8419565529346467, 1.842682974052429, 1.8392709822654725, 
    1.8407804302215576, 1.8396302551269532, 1.8393048126220704, 1.8391339053153992, 1.8389040181159972, 
    1.8381169014453889, 1.8364204421043395, 1.837418332862854, 1.8365260926723481, 1.835582656955719, 
    1.8361218902111054, 1.8360691532611846, 1.8348623941898345, 1.8343311776638032, 1.834995659685135, 
    1.8344802785873413, 1.8339480709552765, 1.83367947101593, 1.8325053750514984, 1.8320177210330963, 
    1.8318493624210357, 1.8318234872341157, 1.8307804188728332, 1.830382324743271, 1.8298563428401946, 
    1.830449243927002, 1.829594289112091, 1.8291221197128296, 1.8282474779129028, 1.8281767003059388, 
    1.8275077984809875, 1.8266849060058594, 1.8271476761341094, 1.8266695246696472, 1.8257972593784333, 
    1.8262487510681151, 1.8256458429813385, 1.82491229968071, 1.8250186491966247, 1.8245329271316528, 
    1.8240152564048766, 1.8235097033023835, 1.8236186639785767, 1.823074847126007, 1.8227150837898254, 
    1.8226096633911133, 1.8222546808242799, 1.822332741165161, 1.821541172361374, 1.821319928741455, 
    1.8210236438751222, 1.8207270562171936, 1.820326228570938, 1.8199907526493073, 1.8197911021709443, 
    1.8195198745727539, 1.8192569496154785, 1.8187607377529145, 1.818500374698639, 1.818333453130722]
loss_mse = [
    2.6355921398162843, 2.0208058394432067, 1.9816112701416015, 1.9438773502826692, 1.902389013671875, 
    1.8892136571884155, 1.8793876215934753, 1.874994971227646, 1.8703722233772277, 1.8668922474384309, 
    1.8622406164169312, 1.859895358133316, 1.855117444753647, 1.8523273648262024, 1.8489683252811433, 
    1.8450799298286438, 1.8423976832389832, 1.8396740611076354, 1.8371101823329925, 1.8346538615703583, 
    1.832023600244522, 1.8308608170986176, 1.8266935180187225, 1.8235928623199462, 1.8220220133304597, 
    1.8192956588745117, 1.819038987827301, 1.816369764328003, 1.8136452107429504, 1.8146585720539092, 
    1.8135151401519776, 1.8098945236206054, 1.8097260770320893, 1.8080198979377746, 1.807180602312088, 
    1.8070106538295745, 1.804743492603302, 1.803359760570526, 1.80378489818573, 1.8033412305831908, 
    1.8013936351776123, 1.8020845617294312, 1.799160105228424, 1.7979140254974366, 1.7984157591342926, 
    1.7974864039421081, 1.7964400978565216, 1.7948475211143493, 1.794806006193161, 1.7948671905994416, 
    1.7940984527111052, 1.7931127223968506, 1.7926292653083802, 1.7909496706485748, 1.7901732441425324, 
    1.7894190918445587, 1.788150149679184, 1.7861221716880797, 1.7847977613925934, 1.7834736835956573, 
    1.7822760798454285, 1.7819205333709718, 1.7807402171611786, 1.7807575165271758, 1.7801062067985534, 
    1.779186518573761, 1.778633508682251, 1.7775394064426422, 1.7772961421966553, 1.776071175146103, 
    1.775543941926956, 1.7741930079460144, 1.7748976885795593, 1.7742194921970367, 1.7744556963920592, 
    1.7720297323703766, 1.772258468914032, 1.7709781210422515, 1.7703344137191772, 1.7698166189193725, 
    1.769481077861786, 1.7687088622570037, 1.7669998180389404, 1.7683846900939941, 1.7658612318992615, 
    1.7651203797340393, 1.7656387555122375, 1.763940172624588, 1.764736679649353, 1.7638068464756012, 
    1.764409337759018, 1.7629791772842407, 1.7634467759609223, 1.761794148683548, 1.7621794661521912, 
    1.76070040102005, 1.759629651927948, 1.7592019804477692, 1.758002365064621, 1.758562369966507, 
    1.7571016711235046, 1.757201210451126, 1.7578352454662323, 1.7552644112110138, 1.7539696964740754, 
    1.7537136501789092, 1.753689035844803, 1.7538379120349885, 1.751878812932968, 1.7523253771305085, 
    1.7519013198375701, 1.750316835451126, 1.7493591747760773, 1.7489820535182954, 1.74743765335083, 
    1.7467936590194701, 1.746813888645172, 1.7457903544425963, 1.7470771846294404, 1.7449899497032166, 
    1.7451255408763886, 1.743478129196167, 1.7429816822052002, 1.7426249308586121, 1.7430664957523345, 
    1.7412200943946838, 1.7413163197040558, 1.7393770518302918, 1.7404172881603241, 1.7383308862686158, 
    1.737613426065445, 1.73763493475914, 1.7367989251613616, 1.7370794194221497, 1.7362711019039154, 
    1.7355234886646271, 1.7341051398277283, 1.7336516202926635, 1.7348428698539733, 1.7327055599212646, 
    1.733728529882431, 1.7333705420970917, 1.7325457701683045, 1.7307550497531892, 1.7304192955493927, 
    1.7310849582672119, 1.7298785229682923, 1.7292070491790772, 1.7297461065769195, 1.7279939287185668, 
    1.7284559233665466, 1.7270922147274017, 1.7279296155452728, 1.726330355167389, 1.7257015329360963, 
    1.7258960678577424, 1.7261922877788545, 1.7257760449886321, 1.725039814043045, 1.7243621199131012, 
    1.7243728033542634, 1.7242533068180084, 1.7229794876098632, 1.7224072489261628, 1.723586839056015, 
    1.7222436335086821, 1.7221605272769929, 1.7219960592269898, 1.720495790576935, 1.7210528072357179, 
    1.7204782980918885, 1.719662666797638, 1.719187972640991, 1.7186049095153808, 1.7190048290252686, 
    1.718560913991928, 1.7181510474681854, 1.718008394575119, 1.7175125345230102, 1.7170113387584687, 
    1.7170842954158783, 1.7167857833385467, 1.7159383111476898, 1.7159096553325652, 1.7153867293834686, 
    1.7156066580295564, 1.7146642708778381, 1.7148086715698243, 1.7141331370353698, 1.713991237449646, 
    1.7135983558177947, 1.7133867614746094, 1.7126670775890351, 1.7128161819934844, 1.7125256472110748, 
    1.7121332437038421, 1.711881921339035, 1.7117531168460847, 1.711321084356308, 1.711233262491226, 
]
loss_ours = [
    2.2349690430641176, 1.963027721118927, 1.9128309205055236, 1.8813277807712554, 1.8548385801315308, 
    1.8249358579158783, 1.8035208092689514, 1.779818851327896, 1.7584545338153839, 1.7372192288398742, 
    1.7183287971496581, 1.7082991224765778, 1.6947058327674867, 1.677065506029129, 1.6685193283081055, 
    1.6609744835853577, 1.6463980905532838, 1.6376935483455657, 1.6316923183918, 1.624654742717743, 
    1.6168004399776459, 1.6139810132026673, 1.6038371015548707, 1.5940146474838257, 1.5923648784160613, 
    1.5798043288230896, 1.5756656147003174, 1.5734784096717835, 1.566783811378479, 1.5633827583789826, 
    1.5602052033901215, 1.5546427721500398, 1.5520494644641876, 1.548988179731369, 1.5427679142951964, 
    1.5381930941581725, 1.5350925498485566, 1.533028022146225, 1.5268859597682953, 1.5265688760757445, 
    1.5219158346652986, 1.5167987483978271, 1.514527166891098, 1.5099501860618592, 1.5093113788604737, 
    1.5039916052341462, 1.50572158908844, 1.4987723653316498, 1.4965910114765166, 1.4974133917808532, 
    1.4934614735603333, 1.4892069345474244, 1.4881280127048493, 1.4853601354122161, 1.4853585989952087, 
    1.479831230211258, 1.4765824236392975, 1.4799408401489258, 1.4739808510780334, 1.4716340727806092, 
    1.4675110411167145, 1.4676539301872253, 1.4652142330646516, 1.4634470564365387, 1.4592016889095307, 
    1.4596622376918793, 1.457911167049408, 1.4570429906845093, 1.460707680797577, 1.4529721735477448, 
    1.449732731437683, 1.4499962114810943, 1.4490718420028688, 1.4472138041496276, 1.4490666917800903, 
    1.4427424734115601, 1.4403479144096374, 1.440454042863846, 1.437898279619217, 1.440431117296219, 
    1.4360447093486786, 1.4337705834388732,
]
plt.figure()
plt.plot(loss_ours)
plt.figure()
plt.plot(loss)
plt.show()