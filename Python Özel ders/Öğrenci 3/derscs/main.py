from PIL import Image, ImageDraw, ImageFont
import textwrap

pic = Image.open('template.png')
draw = ImageDraw.Draw(pic)

font1 = ImageFont.truetype("Gidole-Regular.ttf",40)  
color = "White"

text1 = "abc"
text2 = "asdas"
text3 = "asdasdfas"
text4 = "amdkasmdklmaslkdma"

wrapped_text1 = textwrap.fill(text1,width=20)
wrapped_text2 = textwrap.fill(text2,width=20)
wrapped_text3 = textwrap.fill(text3,width=20)
wrapped_text4 = textwrap.fill(text4,width=20)


pos = [(10,10),(10,160),(10,310),(10,460)]

draw.text1(pos[0],wrapped_text1,fill = color,font= font1)
draw.text2(pos[1],wrapped_text2,fill = color,font= font1)
draw.text3(pos[2],wrapped_text3,fill = color,font= font1)
draw.text4(pos[3],wrapped_text4,fill = color,font= font1)
    
pic.save('out.png')
