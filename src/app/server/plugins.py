from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin
from litestar.plugins.flash import FlashConfig, FlashPlugin  # pyright: ignore[reportUnknownVariableType]
from litestar.plugins.structlog import StructlogPlugin
from litestar_granian import GranianPlugin
from litestar_saq import SAQPlugin
from litestar_vite import VitePlugin
from litestar_vite.inertia import InertiaConfig, InertiaPlugin

from app.config import app as config
from app.server.builder import ApplicationConfigurator

structlog = StructlogPlugin(config=config.log)
vite = VitePlugin(config=config.vite)
saq = SAQPlugin(config=config.saq)
alchemy = SQLAlchemyPlugin(config=config.alchemy)
granian = GranianPlugin()
app_config = ApplicationConfigurator()
inertia = InertiaPlugin(config=InertiaConfig(root_template="site/index.html.j2"))
flasher = FlashPlugin(config=FlashConfig(template_config=vite.template_config))# type: ignore[attr-defined]
