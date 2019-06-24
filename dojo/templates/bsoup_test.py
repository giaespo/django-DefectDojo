from bs4 import BeautifulSoup
import os
import json
import codecs
leaf = {}


if __name__ == '__main__':
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.split('.')[-1] == 'html':
                print(root + '/' + file)
	    
                parsedContent = BeautifulSoup(open(root + '/' + file).read(), 'html.parser')
	            
                # iter will return every node in the document
                #
                paragraphs = parsedContent.findAll()
                for p in paragraphs:
                    txt = p.getText()
                    if ("{%" not in txt) and ("{{" not in txt) and ("$" not in txt) and txt.strip():
                        if file in leaf:
                            leaf[file].append(txt)
                        else:
                            leaf[root + '/' + file] = [txt] 
    
    for el in leaf:
        f = codecs.open(el,'r', "utf-8")
        testo = f.read()
        testo2 = ''
        for t in leaf[el]:
            print(el,t)
            testo2 = testo.replace(t + "<",'{% trans "' + t + '"%}<')
        f.close()
        g = codecs.open(el,'w', "utf-8")
        
        g.write(testo2)
        g.close()
