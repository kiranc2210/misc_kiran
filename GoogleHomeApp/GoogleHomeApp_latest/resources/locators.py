from resources import data
#https://stackoverflow.com/questions/44830028/python-appium-implementing-page-object-model

get_started_btn='com.google.android.apps.chromecast.app:id/primary_button'

choose_account_on_btn='new UiSelector().text("OK")'

Turn_on_wifi_activate_btn='new UiSelector().text("Activate")'

Next_btn= 'new UiSelector().text("Next")'

Turn_on_Wi_Fi='com.google.android.apps.chromecast.app:id/title_text'#'new UiSelector().text("Turn on Wi-Fi")'

primery_btn='com.google.android.apps.chromecast.app:id/primary_button'

turn_on_bluetooth_btn='new UiSelector().text("Turn on")'

allow_alart='new UiSelector().text("ALLOW")'

choose_account='new UiSelector().text("'+data.AccountName+'")'
 
click_plus_icon='com.google.android.apps.chromecast.app:id/home_tab_appbar_add_device_button'

seletup_device= '//android.widget.TextView[@text="Add and manage"]'

new_device_setup_link='new UiSelector().text("New device")'

turn_on_bt_text='new UiSelector().text("Turn on Bluetooth")'

turn_on_wifi_text='new UiSelector().text("Turn on Wi-Fi")'

wifi_alart_toggle_btn='new UiSelector().text("OFF")'

wifi_alart_done='new UiSelector().text("Done")'

What_are_you_setting_up='new UiSelector().text("What are you setting up?")'

not_now='new UiSelector().text("Not now")'


##############POST DEVICE DISCOVERY###############

Lyric_Speaker_Box='new UiSelector().text("Lyric Speaker Box found")'

page_title='com.google.android.apps.chromecast.app:id/title_text'

nearby_devices='new UiSelector().text("Nearby devices")'#

yes_btn='new UiSelector().text("Yes")'

frienldyName='new UiSelector().text("'+data.FriendlyName+'")'

Did_you_hear_the_sound_yes_btn='new UiSelector().text("Yes")'

yes_im_in='new UiSelector().text("Yes, I\'m in")'

Where_is_this_device= 'new UiSelector().text("Where is this device?")'

Next_btn= 'new UiSelector().text("Next")'

Custom_room_name='new UiSelector().text("Where is this device?")'

enter_room_name_txt='com.google.android.apps.chromecast.app:id/text_input_edit_text'

create_a_unique_name='new UiSelector().text("Create a unique name")'

ssid_name='new UiSelector().text("'+data.wifissid+'")'

enter_wifi_password='new UiSelector().text("Enter Wi-Fi password")'

OK_btn= 'new UiSelector().text("OK")'

Wi_Fi_password='new UiSelector().text("Wi-Fi password")'

password_txt='com.google.android.apps.chromecast.app:id/password'

pwd_OK_btn='new UiSelector().text("OK")'

Linking_your_SFLEX101='new UiSelector().text("Linking your Lyric Speaker Box")'

Next_btn= 'new UiSelector().text("Next")'

Continue_btn= 'new UiSelector().text("Continue")'

Connect_btn= 'new UiSelector().text("Connect")'

skip_tutorial_= 'new UiSelector().text("Skip tutorial")'

Finish_tutorial_btn='new UiSelector().text("Finish tutorial")'

try_again='new UiSelector().text("Try again")'

alrt_OK_btn='new UiSelector().text("OK")'

Connect_to_same_Wi_Fi='new UiSelector().text("Connect to same Wi-Fi")'

couldnot_comm_error_msg='new UiSelector().text("We couldn\'t authenticate your Lyric Speaker Box. Please visit support.google.com/chromecast for help troubleshooting this issue.")'

Connection_problem_during_setup='new UiSelector().text("Connection problem during setup")'

tryAgain='new UiSelector().text("Try again")'

cancel='new UiSelector().text("Cancel")'

could_not_authenticate='com.google.android.apps.chromecast.app:id/message'