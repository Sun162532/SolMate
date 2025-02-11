from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    calculation_type = request.form['calculation_type']
    try:
        if calculation_type == 'v/v':
            solute_volume = float(request.form['solute_volume'])
            solution_volume = float(request.form['solution_volume'])
            if solution_volume == 0:
                result = "ปริมาตรของสารละลายต้องไม่เป็นศูนย์"
            else:
                result = f"เปอร์เซ็นต์โดยปริมาตร: {solute_volume / solution_volume * 100:.2f}%"
        elif calculation_type == 'w/w':
            solute_mass = float(request.form['solute_mass'])
            solution_mass = float(request.form['solution_mass'])
            if solution_mass == 0:
                result = "น้ำหนักของสารละลายต้องไม่เป็นศูนย์"
            else:
                result = f"เปอร์เซ็นต์โดยน้ำหนัก: {solute_mass / solution_mass * 100:.2f}%"
        elif calculation_type == 'w/v':
            solute_mass = float(request.form['solute_mass_wv'])
            solution_volume = float(request.form['solution_volume_wv'])
            if solution_volume == 0:
                result = "ปริมาตรของสารละลายต้องไม่เป็นศูนย์"
            else:
                result = f"เปอร์เซ็นต์โดยน้ำหนักต่อปริมาตร: {solute_mass / solution_volume * 100:.2f}%"

        else:
            result = "ประเภทการคำนวณไม่ถูกต้อง"
    except ValueError:
        result = "กรุณากรอกข้อมูลให้ถูกต้อง"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
