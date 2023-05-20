#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
from dotenv import load_dotenv

def configure():
    load_dotenv()


# In[ ]:


import warnings
warnings.filterwarnings('ignore')

import ipywidgets as widgets
from IPython.display import display, clear_output, HTML
color = "#ffcccc"  # choose your desired color

configure()

html_code = f"<style>body{{background-color: {color} !important;}}</style>"


# In[2]:


#!jupyter nbextension enable --py widgetsnbextension --sys-prefix
#!jupyter serverextension enable voila --sys-prefix


# In[3]:


get_ipython().run_cell_magic('html', '', '<style>\n\n@font-face{\n    font-family: "TWKEverett-Hairline";\n    src= url("/Users/ghzhu/Library/Fonts/TWKEverett-Hairline.otf");\n    font-family: "LexendExa-Regular";\n    src= url("/Users/ghzhu/Library/Fonts/LexendExa-Regular.ttf");\n    font-family: "Belleza-Regular";\n    src= url("/Users/ghzhu/Library/Fonts/Belleza-Regular.ttf");\n    font-family: "CrimsonPro-ExtraLightItalic";\n    src= url("/Users/ghzhu/Library/Fonts/CrimsonPro-ExtraLightItalic.ttf");\n    font-family: "CrimsonPro-ExtraLightItalic";\n    src= url("/Users/ghzhu/Library/Fonts/CrimsonPro-Light.ttf");\n    font-family: "Maitree-Light";\n    src= url("/Users/ghzhu/Library/Fonts/Maitree-Light.ttf");\n}\n\n.widget-label {\n    font-size: 10px;\n    font-weight: regular;\n    font-family:"TWKEverett-Hairline";\n} \n\n</style>\n')


# In[ ]:


# Image Widget

file = open("pink.gif", "rb")
image = file.read()

image_headline = widgets.Image(
                    value=image,
                    format='gif',
                    layout=widgets.Layout(width="700px", margin='0 auto')
                )

label_headline = widgets.Label(
                    value='This website is based on :https://github.com/nghweigeok/jupyter_webapp_demo',
                    style={'description_width': 'initial'}
                )

vbox_headline = widgets.VBox([image_headline, label_headline])


# In[ ]:


# name
person = widgets.Text(placeholder="Your name here")
name = widgets.Text(placeholder="Company's name here")


# In[ ]:


import openai
openai.api_key = os.getenv('api_key')


# In[ ]:


# button send

button_send = widgets.Button(
                description='Embrace it!',
                tooltip='Send',
                layout=widgets.Layout(width='100px', margin='0 auto'),
                style={'button_color': 'pink',
                       'font_weight': 'regular',
                       'font_size': '14px',
                       'padding': '10px 20px',
                       'border_radius': '10px',
                       'font_family': 'Maitree-Light'}
                )

output = widgets.Output(layout=widgets.Layout(text_align='center', max_width = '700px'))

def on_button_clicked(event):
    response = openai.Completion.create(
    model="curie:ft-personal-2023-04-26-03-19-16",
    prompt=f"{name.value}",
    temperature=0.6, #randomness 
    max_tokens=80, #charaters in response 
    top_p=1, #controls diversity
    frequency_penalty=0.5, #decrease repetition 
    presence_penalty=0.5 #increase likelihood to talk about new topic 
)
    result = response.choices[0].text
    with output:
        clear_output()
        print(f"Dear {person.value},\n")
        print(result)
        print("")
        print(f"Sincerely,")
        print(f"{name.value} Recruiting Team")

button_send.on_click(on_button_clicked)

vbox_result = widgets.VBox([button_send, output], layout=widgets.Layout(justify_content='center'))


# In[ ]:


# stacked right hand side

text_0 = widgets.HTML(value="<h1 style='font-family: CrimsonPro-ExtraLightItalic; font-size: 48px; text-align: center;'>♡₊˚ 🦢 Rejection Therapy・₊✧</h1>")
text_1 = widgets.HTML(value="<h2 style='font-family: Belleza-Regular; font-size: 30px;text-align: center;'>Please type your dream company ‧₊˚ 🍮 ⋅ ☆</h2>")
text_4 = widgets.HTML(value="<h3 style='font-family: CrimsonPro-ExtraLightItalic; font-size: 18px; text-align: center;'>Congratulations! Are you ready to have a beautiful rejection letter from your dream position? <br>Enjoy it!</h2>")

name.style.description_width = 'initial'
name.layout.width = '200px'
name.layout.margin = '0 auto'
person.style.description_width = 'initial'
person.layout.width = '200px'
person.layout.margin = '0 auto'

vbox_text = widgets.VBox([ image_headline, label_headline, text_0, person, text_1, name, text_4, vbox_result])


# In[ ]:


page = widgets.HBox([vbox_text], layout=widgets.Layout(justify_content='center'))
display(widgets.VBox([page], layout=widgets.Layout(justify_content='center')))
display(HTML(html_code))


# In[10]:


pip install session-info


# In[11]:


import session_info
session_info.show()


# In[ ]:




