from Crypto.Util.number import long_to_bytes
import gmpy2
# Different parameters for each team
N = 14922959775784066499316528935316325825140011208871830627653191549546959775167708525042423039865322548420928571524120743831693550123563493981797950912895893476200447083386549353336086899064921878582074346791320104106139965010480614879592357793053342577850761108944086318475849882440272688246818022209356852924215237481460229377544297224983887026669222885987323082324044645883070916243439521809702674295469253723616677245762242494478587807402688474176102093482019417118703747411862420536240611089529331148684440513934609412884941091651594861530606086982174862461739604705354416587503836130151492937714365614194583664241
e2 = 27188825731727584656624712988703151030126350536157477591935558508817722580343689565924329442151239649607993377452763119541243174650065563589438911911135278704499670302489754540301886312489410648471922645773506837251600244109619850141762795901696503387880058658061490595034281884089265487336373011424883404499124002441860870291233875045675212355287622948427109362925199018383535259913549859747158348931847041907910313465531703810313472674435425886505383646969400166213185676876969805238803587967334447878968225219769481841748776108219650785975942208190380614555719233460250841332020054797811415069533137170950762289
e1 = 114552459553730357961013268333698879659007919035942930313432809776799669181481660306531243618160127922304264986001501784564575128319884991774542682853466808329973362019677284072646678280051091964555611220961719302320547405880386113519147076299481594997799884384012548506240748042365643212774215730304047871679706035596550898944580314923260982768858133395187777029914150064371998328788068888440803565964567662563652062845388379897799506439389461619422933318625765603423604615137217375612091221578339493263160670355032898186792479034771118678394464854413824347305505135625135428816394053078365603937337271798774138959
c = 6472367338832635906896423990323542537663849304314171581554107495210830026660211696089062916158894195561723047864604633460433867838687338370676287160274165915800235253640690510046066541445140501917731026596427080558567366267665887665459901724487706983166070740324307268574128474775026837827907818762764766069631267853742422247229582756256253175941899099898884656334598790711379305490419932664114615010382094572854799421891622789614614720442708271653376485660139560819668239118588069312179293488684403404385715780406937817124588773689921642802703005341324008483201528345805611493251791950304129082313093168732415486813
alpha2 = 730/2048
M1 = int(gmpy2.mpz(N)**0.5)
M2 = int( gmpy2.mpz(N)**(1+alpha2) )
D = diagonal_matrix(ZZ, [N, M1, M2, 1])
B = Matrix(ZZ, [[1, -N,   0,  N**2],
                [0, e1, -e1, -e1*N],
                [0,  0,  e2, -e2*N],
                [0,  0,   0, e1*e2]]) * D
L = B.LLL()
v = Matrix(ZZ, L[0])
x = v * B**(-1)
phi = (x[0,1]/x[0,0]*e1).floor()

PR = PolynomialRing(ZZ, 'x')
x = PR.gen()
f = x**2 - (N-phi+1)*x + N
p = f.roots()[0][0]
print(p)
q = int(N) // int(p)
d = inverse_mod( 65537, (p-1)*(q-1) )
m = power_mod(c, d, N)
print(b'flag: ' + long_to_bytes(m))