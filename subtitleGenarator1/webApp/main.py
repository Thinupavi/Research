import os

from flask import Flask, request, render_template, url_for
import scripts.runner_vtt as runner_vtt
import scripts.runner_vtt_from_local_file as run_local_file

VTT_FILE_PATH = os.path.join('static', 'SubtitleFile')
app = Flask(__name__)
app.config['VTT_FOLDER'] = VTT_FILE_PATH


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/generateSub', methods=["GET", "POST"])
def generateSub():
    if request.method == 'POST':

        url = request.form['url']
        lang = request.form['lang']

        if lang in 'Tamil':
            apiLan = 'ta'
        if lang in 'Sinhala':
            apiLan = 'si'

        print(lang)
        videoName, vttFileName = runner_vtt.genarateSUB(url, apiLan)
        vttFile = os.path.join(app.config['VTT_FOLDER'], vttFileName)
        urlVid = 'http://localhost/SubtitleGenaretor/Videos/' + videoName + '.mp4'

        # vttFile = os.path.join(app.config['VTT_FOLDER'], 'SharingyourGoogledatawithApps-New_si.vtt')
        # urlVid = 'http://localhost/SubtitleGenaretor/Videos/SharingyourGoogledatawithApps-New.mp4'

        return render_template('video.html', vttFile=vttFile, language=lang, urlVid=urlVid)

    return render_template('index.html')


@app.route("/upload", methods=["POST"])
def upload():

    target = 'C:/xampp/htdocs/SubtitleGenaretor/Videos/'
    print(target)
    # if not os.path.isdir(target):
    #     os.mkdir(target)
    print(request.files.getlist("file"))
    lang = request.form['lang']
    print(lang)
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename

        # This is to verify files are supported
        ext = os.path.splitext(filename)[1]
        if (ext == ".mp4"):
            print("File supported moving on...")
        else:
            render_template("Error.html", message="Files uploaded are not supported...")
        destination = "/".join([target, str(filename).replace(" ", "")])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)
        vttFileName = run_local_file.genarateSUB(destination, str(filename).replace(" ", "").replace('.mp4', ''), lang)

        vttFile = os.path.join(app.config['VTT_FOLDER'], vttFileName)
        urlVid = 'http://localhost/SubtitleGenaretor/Videos/' + str(filename).replace(" ", "")

    # return send_from_directory("images", filename, as_attachment=True)
    return render_template('video.html', vttFile=vttFile, language=lang, urlVid=urlVid)


if __name__ == "__main__":
    app.run(debug=True)
