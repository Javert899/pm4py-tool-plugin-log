import pm4pytoollogplugin
import preload
import os

if __name__ == "__main__":
    preload.preload()
    app = pm4pytoollogplugin.app
    app.static_folder = os.path.join(os.getcwd(), "html")
    app.run()
