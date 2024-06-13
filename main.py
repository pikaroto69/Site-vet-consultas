from flask import Flask, request, jsonify, render_template, request, redirect

app = Flask(__name__)




#Vitor2

@app.route('/')
def home():
    return render_template('index.html')


#------

consultas = []

@app.route('/consultass')
def consultass():
    return render_template('consultas.html', consultas=consultas)

@app.route('/abrir_consultas')
def abrir_consultas():
    return render_template('adicionar_consulta.html')

@app.route('/adicionar_consulta', methods=['GET', 'POST'])
def adicionar_consulta():
    """
    Rota para adicionar um novo contato.
    Se o método for POST, adiciona o novo contato à lista.
    Se não, exibe o formulário para adicionar um novo contato.
    """
    if request.method == 'POST':
        nome = request.form['nome']
        animal = request.form['animal']
        data = request.form['data']
        sintoma = request.form['sintoma']
        codigo = len(consultas)
        consultas.append([codigo, nome, animal, data, sintoma])
        return redirect('/consultass')  # Redireciona de volta para a página inicial
    else:
        return render_template('adicionar_consulta.html')  # Renderiza o formulário de adicionar contato

@app.route('/editar_consulta/<int:codigo>', methods=['GET', 'POST'])
def editar_consulta(codigo):
    """
    Rota para editar um contato existente.
    Se o método for POST, atualiza os detalhes do contato com o ID fornecido.
    Caso contrário, exibe o formulário preenchido com os detalhes do contato para edição.
    """
    if request.method == 'POST':
        nome = request.form['nome']
        animal = request.form['animal']
        data = request.form['data']
        sintoma = request.form['sintoma']
        consultas[codigo] = [codigo, nome, animal, data, sintoma]
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        consulta = consultas[codigo]
        return render_template('editar_consulta.html', consulta=consultas)  # Renderiza o formulário de edição

@app.route('/apagar_consulta/<int:codigo>')
def apagar_consulta(codigo):
    del consultas[codigo]
    return redirect('/')  # Redireciona de volta para a página inicial

#Arthur 1

@app.route('/mostrar_calcular_idade')
def mostrar_calcular_idade():
    return render_template('calcular_idade_humana.html',idade = '') 


@app.route('/calcular_idade_humana', methods=['GET', 'POST'])
def calcular_idade_humana():
    especie = request.form['especie']
    idade_animal = int(request.form['idade_animal'])
    idade = 0
    if request.method == 'POST':
        if especie.lower() == 'cachorro':
            if idade_animal == 1:
                idade = 7
            elif idade_animal == 2:
                idade = 14
            elif idade_animal == 3:
                idade = 21
            elif idade_animal == 4:
                idade = 28
            elif idade_animal == 5:
                idade = 35
            elif idade_animal >= 6:
                idade = 35 + (idade_animal - 5) * 5
        elif especie.lower() == 'gato':
            if idade_animal == 1:
                idade = 12
            elif idade_animal == 2:
                idade = 25
            elif idade_animal == 3:
                idade = 29
            elif idade_animal == 4:
                idade = 33
            elif idade_animal == 5:
                idade = 37
            elif idade_animal >= 6:
                idade = 37 + (idade_animal - 5) * 4
        else:
            idade = "Espécie não suportada para o cálculo de idade humana."

        return render_template('calcular_idade_humana.html', idade= idade)
    return redirect('/')




#vitor

@app.route('/inde', methods=['GET', 'POST'])
def inde():
    if request.method == 'POST':
        grau = request.form['grau']
        peso = float(request.form['peso'])

        if grau == 'leve':
            volume = 50 * peso
        elif grau == 'moderada':
            volume = 75 * peso
        elif grau == 'grave':
            volume = 100 * peso
        else:
            volume = 0

        return render_template('inde.html', volume=volume)

    return render_template('inde.html', volume=0)


#Joao pedro


pacientes = []

@app.route('/indez')
def indez():
    return render_template( 'indez.html', pacientes=pacientes)

@app.route('/adicionar_paciente', methods=['GET', 'POST'])
def adicionar_pacientes():
    if request.method == 'POST':
        nome = request.form['nome']
        raca = request.form['raca']
        peso = request.form['peso']
        nometutor = request.form['nometutor']
        especie = request.form['especie']
        telefone = request.form['telefone']
        codigo = len(pacientes)
        pacientes.append([codigo, nome, telefone, raca, peso, nometutor, especie])
        return redirect('/indez')
    else:
        return render_template('adicionar_paciente.html')

@app.route('/editar_paciente/<int:codigo>', methods=['GET', 'POST'])
def editar_pacientes(codigo):
    """
    Rota para editar um contato existente.
    Se o método for POST, atualiza os detalhes do contato com o ID fornecido.
    Caso contrário, exibe o formulário preenchido com os detalhes do contato para edição.
    """
    if request.method == 'POST':
        nome = request.form['nome']
        raca = request.form['raca']
        peso = request.form['peso']
        nometutor = request.form['nometutor']
        especie = request.form['especie']
        telefone = request.form['telefone']
        pacientes[codigo] = [codigo, nome, telefone, peso, raca, especie, nometutor]
        return redirect('/indez')  # Redireciona de volta para a página inicial
    else:
        paciente = pacientes[codigo]
        return render_template('editar_paciente.html', paciente=paciente)  # Renderiza o formulário de edição

@app.route('/apagar_paciente/<int:codigo>')
def apagar_pacientes(codigo):
    """
    Rota para apagar um contato da lista.
    """
    del pacientes[codigo]
    return redirect('/indez')  # Redireciona de volta para a página inicial





#Arthur 2

@app.route('/peso_medicamento')
def peso_medicamento():
    return render_template('peso_medicamento.html', dose=0)

@app.route('/calcular_dose_medicamento', methods=['GET', 'POST'])
def calcular_dose_medicamento():
    if request.method == 'POST':
        peso_animal = float(request.form['peso_animal'])
        dose_recomendada = float(request.form['dose_recomendada'])

        dose = peso_animal * dose_recomendada

        return render_template('peso_medicamento.html', dose=dose)

    return redirect('/peso_medicamento')



if __name__ == '__main__':
    app.run(debug=True)

