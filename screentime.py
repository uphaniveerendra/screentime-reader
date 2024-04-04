from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import subprocess

class ScreenTimeApp(App):
    def __init__(self, **kwargs):
        super(ScreenTimeApp, self).__init__(**kwargs)
        self.app_usage_data = {}

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="App Name: Screen Time")
        layout.add_widget(self.label)
        return layout

    def on_start(self):
        self.update_screen_time()

    def update_screen_time(self):
        adb_command = "adb shell dumpsys usagestats | grep 'Microsoft Store'"
        process = subprocess.Popen(adb_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        usage_time = stdout.decode("utf-8").strip()
        self.label.text = f"App Name: Screen Time\nUsage Time: {usage_time}"

if __name__ == '__main__':
    ScreenTimeApp().run()
