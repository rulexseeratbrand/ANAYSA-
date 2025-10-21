from flask import Flask, request, render_template_string, abort

import requests

import random

import time

app = Flask(name)



Define your Facebook API endpoint and headers

API_URL = 'https://graph.facebook.com/v15.0/'

HEADERS = {

'Connection': 'keep-alive',

'Cache-Control': 'max-age=0',

'Upgrade-Insecure-Requests': '1',

'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',

'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8',

'Accept-Encoding': 'gzip, deflate',

'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',

'referer': 'www.google.com'

}

Define a function to send messages to Facebook conversations

def send_messages(access_tokens, thread_id, hater_name, messages, delay):

while True:

for token in access_tokens:







       try:







           random_message = random.choice(messages).strip()







           message_text = f'{hater_name} {random_message}'







           parameters = {'access_token': token, 'message': message_text}







           response = requests.post(f'{API_URL}t_{thread_id}/', data=parameters, headers=HEADERS)







           if response.status_code == 200:







               print(f"Message sent using token {token}: {message_text}")







           else:







               print(f"Failed to send message using token {token}: {message_text}")







       except Exception as e:







           print(f"Error while sending message using token {token}: {message_text}")







           print(e)







       time.sleep(delay)

@app.route('/', methods=['GET', 'POST'])

def home():

if request.method == 'POST':

access_tokens_file = request.files['tokensFile']







   access_tokens = access_tokens_file.read().decode().splitlines()







   thread_id = request.form.get('threadId')







   hater_name = request.form.get('haterName')







   txt_file = request.files['txtFile']







   delay = int(request.form.get('time'))







   messages = txt_file.read().decode().splitlines()







   send_messages(access_tokens, thread_id, hater_name, messages, delay)

return render_template_string('''

<!DOCTYPE html><html lang="en"><head>   <meta charset="utf-8">   <meta name="viewport" content="width=device-width, initial-scale=1.0">   <title>Anvi | Ofline</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">   <style>
  

  

  

  
       .container {
  
    max-width: 500px;
  
    background: linear-gradient(135deg, #ff69b4, #6a0dad);
  
    border-radius: 10px;
  
    padding: 20px;
  
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  
    margin: 0 auto;
  
    margin-top: 20px;
  
}
  

  

  
body {
  
    margin: 0;
  
    padding: 0;
  
    height: 100vh;
  
    background: linear-gradient(-45deg, #000000, #4b0082, #8a2be2);
  
    background-size: 400% 400%;
  
    animation: gradientBG 10s ease infinite;
  
}
  

  
/* Gradient Animation Keyframes */
  
@keyframes gradientBG {
  
    0% { background-position: 0% 50%; }
  
    50% { background-position: 100% 50%; }
  
    100% { background-position: 0% 50%; }
  
}
  

  

  

  

  
      .header h1 {
  
    text-align: center;
  
    margin-bottom: 20px;
  
    color: #ffffff; /* white text */
  
    text-shadow: 2px 2px 8px rgba(255, 105, 180, 0.7); /* pink glow */
  
}
  

  

  

  

  
       .header img {
  

  

  

  
           max-width: 100px; /* Adjust as needed */
  

  

  

  
           margin-right: 100px;
  

  

  

  
       }
  

  

  

  
       .random-img {
  

  

  

  
           max-width: 300px; /* Adjust image size as needed */
  

  

  

  
           margin: 100px;
  

  

  

  
       }
  

  

  

  
       /* Add more CSS styles for other elements as needed */
  

  

  

  
       /* For example, you can use classes to style form elements and buttons */
  

  
/* Common input styling */
  
input[type="text"],
  
input[type="number"],
  
textarea {
  
    width: 100%;
  
    padding: 12px;
  
    margin-bottom: 15px;
  
    border: 2px solid transparent;
  
    border-radius: 8px;
  
    box-sizing: border-box;
  
    background: rgba(255, 255, 255, 0.1); /* glassmorphism effect */
  
    color: #fff;
  
    font-size: 16px;
  
    outline: none;
  
    transition: all 0.4s ease;
  
}
  

  
/* Gradient border and glow on focus */
  
input[type="text"]:focus,
  
input[type="number"]:focus,
  
textarea:focus {
  
    border-image: linear-gradient(90deg, #ff69b4, #6a0dad) 1;
  
    border-width: 2px;
  
    background: rgba(255, 255, 255, 0.15);
  
    box-shadow: 0 0 12px rgba(255, 105, 180, 0.8), 0 0 20px rgba(106, 13, 173, 0.7);
  
}
  

  
/* For .form-control class */
  
.form-control {
  
    width: 100%;
  
    padding: 12px;
  
    margin-bottom: 15px;
  
    border: 2px solid transparent;
  
    border-radius: 8px;
  
    background: rgba(255, 255, 255, 0.1);
  
    color: #fff;
  
    font-size: 16px;
  
    transition: all 0.4s ease;
  
}
  

  
.form-control:focus {
  
    border-image: linear-gradient(90deg, #ff69b4, #6a0dad) 1;
  
    box-shadow: 0 0 12px rgba(255, 105, 180, 0.8), 0 0 20px rgba(106, 13, 173, 0.7);
  
}
  

  
     
  
input[type="submit"] {
  
    width: 100%;
  
    padding: 12px;
  
    font-size: 16px;
  
    font-weight: bold;
  
    color: #fff;
  
    border: none;
  
    border-radius: 8px;
  
    cursor: pointer;
  
    background: linear-gradient(90deg, #ff69b4, #6a0dad);
  
    box-shadow: 0 0 10px rgba(255, 105, 180, 0.6), 0 0 20px rgba(106, 13, 173, 0.5);
  
    transition: all 0.4s ease;
  
}
  

  
/* Hover effect with shine */
  
input[type="submit"]:hover {
  
    background: linear-gradient(90deg, #6a0dad, #ff69b4);
  
    box-shadow: 0 0 15px rgba(255, 105, 180, 0.9), 0 0 25px rgba(106, 13, 173, 0.8);
  
    transform: scale(1.05);
  
}
  

  
.footer {
  

  
         
  
margin-top: 20px;
  

  
          color: #fff;
  

  
           text-align: center;
  

  
           padding: 20px;
  

  
           bottom: 0;
  

  
           left: 0;
  

  
           width: 100%;
  
     }
  

  
       .btn-submit {
  

  

  

  
           
  

  
width: 100%;
  
margin-top: 10px;
  

  
           color: white;
  

  

  

  
           padding: 10px 20px;
  

  

  

  
           border: none;
  

  

  

  
           cursor: pointer;
  

  

  

  
       }
  
     
  
     input[type="submit"]:hover {
  

  
           background-color: #0056b3;
  
       
  
     }
  
     
  
     
  
.image-container img {
  

  
           max-width: 100%;
  

  
           height: auto;
  

  
           display: block;
  

  
           margin: 0 auto;
  

  
       }
  
     .whatsapp-link {
  
display: inline-block;
  

  
   color: #25d366;
  

  
   text-decoration: none;
  

  
   margin-top: 10px;
  
     }
  
.whatsapp-link i {
  

  
   margin-right: 5px;
  
     }
  
   </style></head><body><header class="header mt-4"><div class="container">

    <div class="image-container"> <img src="https://i.imgur.com/MjbRl4m.png" alt="Image">

        <h1 class="mt-3" style="font-size: 2.5rem; font-weight: bold; color: #fff; text-shadow: 0 0 10px #ff69b4, 0 0 20px #6a0dad;">

            Anvi (XD)

        </h1>

    </div>

</div>

</header>   <div class="container"><form action="/" method="post" enctype="multipart/form-data">







       <div class="mb-3">

<div class="mb-3"><label for="tokensFile" style="color: blue;">

    <i class="fa-solid fa-file-upload"></i> Upload Your Tokens File:

</label>

<input type="file" class="form-control" id="tokensFile" name="tokensFile" required>

</div><div class="mb-3"><label for="threadId" style="color: black;">

    <i class="fa-solid fa-hashtag"></i> Thread ID:

</label>

<input type="text" class="form-control" id="threadId" name="threadId" required>

</div><div class="mb-3"><label for="haterName" style="color: black;">

    <i class="fa-solid fa-user-slash"></i> Hater's Name:

</label>

<input type="text" class="form-control" id="haterName" name="haterName" required>

</div><div class="mb-3"><label for="txtFile" style="color: black;">

    <i class="fa-solid fa-file-lines"></i> Upload Abuse File:

</label>

<input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>

</div><div class="mb-3"><label for="time" style="color: black;">

    <i class="fa-solid fa-clock"></i> Delay:

</label>

<input type="number" class="form-control" id="time" name="time" required>

</div><button type="submit" class="btn btn-primary btn-submit"><i class="fa-solid fa-play"></i> Thread Start

</button></form>

   </div><footer class="footer"><p>© 2025 All Rights Reserved | <span>Anvi Private Server</span></p>

</footer></body></html>''')

if name == 'main':

app.run(host='0.0.0.0', port=5000)
