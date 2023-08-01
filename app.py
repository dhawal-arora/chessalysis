import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import io
import threading
from flask import Flask, render_template, request, Response
from pytchat import core as pycore
from pytchat.util import extract_video_id
from movefilter import pawn,piece
app = Flask(__name__)

def update_chart(moves, ax):
    filtered_moves = [move for move in moves]
    uniquemoves = list(set(filtered_moves))
    listofoccurrences = [filtered_moves.count(move) for move in uniquemoves]
    ax.clear()
    ax.bar(uniquemoves, listofoccurrences)
    ax.set_xlabel('Messages')
    ax.set_ylabel('Number of Occurrences')
    ax.set_title('Live Stream Chat Messages (Character Length < 20)')
    ax.tick_params(axis='x', rotation=45)

    # Set the y-axis ticks to whole numbers
    max_occurrences = max(listofoccurrences) if listofoccurrences else 0
    y_ticks = range(0, max_occurrences + 1)
    ax.set_yticks(y_ticks)

def chat_listener(videoid, moves, running):
    _vid = extract_video_id(videoid)
    chat = pycore.PytchatCore(_vid, interruptable=False)

    while running[0]:
        for c in chat.get().sync_items():
            print (c.message)
            if c.message[0] in ["a","b","c","d","e","f","g","h"] and 1<len(c.message)<6:
                pawn(c.message,moves)
            elif c.message[0] in ["R","N","B","Q","K"] and 2<len(c.message)<7:
                piece(c.message,moves) 

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_link = request.form["video_link"]
        video_id = extract_video_id(video_link)

        fig, ax = plt.subplots()
        moves = []
        running = [True]

        chat_thread = threading.Thread(target=chat_listener, args=(video_id, moves, running))
        chat_thread.start()

        def generate_chart():
            while running[0]:
                update_chart(moves, ax)
                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                yield (b'--frame\r\n'
                       b'Content-Type: image/png\r\n\r\n' + buf.getvalue() + b'\r\n')

        return Response(generate_chart(), content_type='multipart/x-mixed-replace; boundary=frame')
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
