from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimo
from .forms import CadastroLivro, CategoriaLivro



def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session.get('usuario'))
        livros = Livros.objects.filter(usuario=usuario)
        status_categoria = request.GET.get('status_categoria')

        form = CadastroLivro()
        form_categoria = CategoriaLivro()
        form.fields['usuario'].initial = request.session.get('usuario')
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)
        return render(request, 'home.html', {'livros': livros,
                                             'usuario_logado': request.session.get('usuario'),
                                             'form': form,
                                             'form_categoria': form_categoria,
                                             'status_categoria': status_categoria})
    else:
        return redirect('/auth/login/?status=2')


def ver_livro(request, id):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session.get('usuario'))
        livro = Livros.objects.get(id=id)
        form = CadastroLivro()
        form.fields['usuario'].initial = request.session.get('usuario')
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)


        form_categoria = CategoriaLivro()

        if request.session.get('usuario') == livro.usuario.id:
            categoria_livro = Categoria.objects.filter(usuario_id=request.session.get('usuario'))
            emprestimo = Emprestimo.objects.filter(livro=livro)
            return render(request, 'ver_livro.html',
                          {'livro': livro, 'categoria_livro': categoria_livro,
                           'emprestimo': emprestimo,
                           'usuario_logado': request.session.get('usuario'),
                           'form': form,
                           'id_livro': id,
                           'form_categoria': form_categoria})
        else:
            return HttpResponse('Esse livro não é seu')
    return redirect('/auth/login/?status=2')


def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/livro/home')
        else:
            return HttpResponse('Dados Inválidos')


def excluir_livro(request, id):
    Livros.objects.get(id=id).delete()
    return redirect('/livro/home')


def cadastrar_categoria(request):
    form = CategoriaLivro(request.POST)
    nome = form.data['nome']
    descricao = form.data['descricao']
    id_usuario = request.POST.get('usuario')
    if int(id_usuario) == int(request.session.get('usuario')):
        user = Usuario.objects.get(id=id_usuario)
        categoria = Categoria(nome=nome, descricao=descricao, usuario=user)
        categoria.save()
        return redirect('/livro/home?status_categoria=1')
    else:
        return HttpResponse("error")

