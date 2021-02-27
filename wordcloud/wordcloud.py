import os

words={
    "genome. ":70,
    "repins. ":105,
    "cluster. ":50,
    "extragenic space. ": 35,
    "common ancestor. ":46,
    "selfish genetic elements. ":27,
    "repetitive sequence. ":49,
    "sequence similarity. ":39,
    "host genome. ":55,
    "coevolution. ": 40,
    "Fig Wasp. ":61,
    "nymph. ":53,
    "mutation. ":61,
    "natural selection. ":83,
    "fitness landscape. ":56,
    "survival. ": 34,
    "mobile genetic elements. ": 18,
    "keystone. ": 12,
    "population. ": 39,
    "adaptation. ": 58,
    "RAYTs. ": 20,
    "probosis. ": 10,
    "camouflage. ":24,
    "chloraphis. ":41,
    "flanking sequence. ": 9,
    "biodiversity. ": 23,
    "collective behaviour. ": 49,
    "handicap principle. ": 7,
    "generation. ": 24,
    "species. ": 51,
    "phylogeny. ": 61,
    "natural history. ": 43,
    "sexual selection. ": 25,
    "genetic drift. ": 49,
    "polymorphism. ": 15,
    "equilibrium. ": 12,
    "diverge. ": 9,
    "speciation. ": 23,
    "selection pressure. ": 59,
    "advantage. ": 31,
    
}

fx=open("wordcloud_content.txt","w+")
fx.write(" ".join([words[i]*i for i in words.keys()]))
fx.close()
os.system("open wordcloud_content.txt")