import util
from multiprocessing import Pool

links = util.get_all_links('http://www.seriouseats.com/user/profile/Goodeaterkenji',20)
p = Pool(8)
p.map(util.get_all_images,links)
