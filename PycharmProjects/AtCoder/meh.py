import itertools
import math
'''from Crypto.Util.number import getPrime, bytes_to_long

def prod(lst):
    ret = 1
    for num in lst:
        ret *= num
    return ret


s = 5063044818262689349546481067052560277152768583825797461048343533234972879239682659155894702765781959079059082984180815182574418440572589398433071983557250741951706997461200682654263844788610562573902643381085125976082911294476910155786547493524567231063893110746852349278093493676517767429281515526243583180149919787431112177379704118607502476646097739215044375652078206758127750408292353473677676942875580799403593608239135605307923598655237414878299381511822118457743459711574878291024456900481855007946459091382645700364836778416412720674300534200173875498954894297558726799070654115564322285197448853366633464568677410728501877583102809033848558601197433765401159269846371331652281165634000155777927063299110580323061291654757690658347384655841929618150310860319222676939967572620107832276316304925998118139293762311660071240329782138957362770088691273787358830040621104775963704507191818542565885405938633849553474747184699776816692963098840666843038183442042916232475516202316840679354482839093385626076296376333652878742150358231943536875543518175278329634124185393227633488627151178677901966478684565832316685226626428651627591996365040234526464928756930330004873367220895028105589453914590291325257828519729315640629897212089539145769625632189125456455778939633021487666539864477884226491831177051620671080345905237001384943044362508550274499601386018436774667054082051013986880044122234840762034425906802733285008515019104201964058459074727958015931524254616901569333808897189148422139163755426336008738228206905929505993240834181441728434782721945966055987934053102520300610949003828413057299830995512963516437591775582556040505553674525293788223483574494286570201177694289787659662521910225641898762643794474678297891552856073420478752076393386273627970575228665003851968484998550564390747988844710818619836079384152470450659391941581654509659766292902961171668168368723759124230712832393447719252348647172524453163783833358048230752476923663730556409340711188698221222770394308685941050292404627088273158846156984693358388590950279445736394513497524120008211955634017212917792675498853686681402944487402749561864649175474956913910853930952329280207751998559039169086898605565528308806524495500398924972480453453358088625940892246551961178561037313833306804342494449584581485895266308393917067830433039476096285467849735814999851855709235986958845331235439845410800486470278105793922000390078444089105955677711315740050638
primes = [getPrime(32) for _ in range(128)]
n = prod(primes)
e = 65537
print(n)
print(pow(m, e, n))'''
n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
primes = set()
for k in arr:
    