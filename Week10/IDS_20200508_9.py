cast = ['Robert Downey Jr.', 'Chris Evans', 'Mark Ruffalo', 'Chris Hemsworth', 'Scarlett Johansson', 'Jeremy Renner', 'Don Cheadle', 'Paul Rudd', 'Benedict Cumberbatch', 'Chadwick Boseman', 'Brie Larson', 'Tom Holland', 'Karen Gillan', 'Zoe Saldana', 'Evangeline Lilly']
print("將飾演奇異博士（Doctor Strange）的演員用選出來")
#索引(從開頭數)
print(cast[8]) 
#索引(從末端數)
print(cast[-7]) 
print("=========================")
print("將第一集復仇者聯盟的六位英雄選出來")
#索引(從開頭數)
i = 0 
while i <= 5:
    print(cast[i])
    i += 1
print("-------------------------")
#索引(從末端數)
i = -10
while i >= -15:
    print(cast[i])
    i -= 1
print("-------------------------")
print(len(cast))
#切割
print(cast[:6]) 

