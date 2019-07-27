from flask import Flask
from System import System
from User import User

app = Flask(__name__)
app.secret_key = 'very-secret-123'  # Used to add entropy

system = System()
u1 = User("Jaiki", "pw")
u2 = User("Ajay", "pw")
u3 = User("Takumi", "pw")

system.addNewPost("Sports Arts", "Sports are recreational activities played by competitors around the world. Popular team sports include soccer, basketball, and baseball. ... By incorporating pieces from our collection of sports art, you can represent athleticism and healthy forms of exercise.", u1, ["Arts", "Sports"])
system.addNewPost("History Of Rugby", "The origin of rugby football is reputed to be an incident during a game of English school football at Rugby School in 1823, when William Webb Ellis is said to have picked up the ball and run with it. ... Old Rugbeian Albert Pell, a student at Cambridge, is credited with having formed the first rugby team.", u2, ["History", "Sports"])
system.addNewPost("History Of Arts", "Art history is the study of objects of art in their historical development and stylistic contexts; that is genre, design, format, and style. The study includes painting, sculpture, architecture, ceramics, furniture, and other decorative objects.", u3, ["History", "Arts"])