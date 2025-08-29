from rest_framework.routers import DefaultRouter
# Nessa linha importar os viewsets

router = DefaultRouter()
# Nessa linha registrar os viewsets
# Exemplo: router.register(r'nome_do_modelo', NomeDoModeloViewSet)

urlpatterns = router.urls
