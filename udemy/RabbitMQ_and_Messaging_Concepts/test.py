import logging

from sanic_routing import BaseRouter

logging.basicConfig(level=logging.DEBUG)


class Router(BaseRouter):
    def get(self, path, *args, **kwargs):
        return self.resolve(path, *args, **kwargs)


router = Router()

router.add("/<foo>", lambda: ...)
router.finalize()
router.tree.display()
logging.info(router.find_route_src)

route, handler, params = router.get("/matchme", method="BASE", extra=None)