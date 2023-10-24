from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, AlunoSerializerV2, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.response import Response
from rest_framework import status

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    #muda de acordo com o query para v1 ou v2
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunoSerializerV2
        else:
            return AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    #recriando a função create
    def create(self, request):
        #buscando todos dados da requisição
        serializer = self.serializer_class(data=request.data)
        #verifica se é valido e salva
        if serializer.is_valid():
            serializer.save()
            #cria uma resposta HTTP indicando que o recurso foi criado com sucesso
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            #procura o id e transforma em string
            id = str(serializer.data['id'])
            #concatena o endereço completo com o id e adiciona ao cabeçalho "Location" da resposta
            response['Location'] = request.build_absolute_uri() + id
            return response


class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matrículas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    #colocando apenas os metodos http desejados para aparecer
    http_method_names = ['get', 'post', 'put', 'patch']
    
    

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer