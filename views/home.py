import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from service.feed_generator import urls

templates = Jinja2Templates(directory="templates")

router = fastapi.APIRouter()


@router.get("/")
def index(request: Request):
    context_data = {'request': request, 'urls': urls}
    return templates.TemplateResponse('home/index.html', context=context_data)


@router.get("/favicon.ico")
def favicon():
    return fastapi.responses.RedirectResponse(url="/static/img/favicon.ico")
