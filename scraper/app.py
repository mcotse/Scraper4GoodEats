import util
import sys
from multiprocessing import Pool

url = sys.argv[0]
#how many pages to extend
extend_page = sys.argv[1]

links = util.get_all_links(sys.argv[0],sys.argv[1])
p = Pool(4)
p.map(util.get_all_images,links)
