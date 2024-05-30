import pysikuli as sik
import time
from pynput.keyboard import Key

# image = sik.find(image="b.png", max_search_time=30)
# sik.click("d.JPG", precision=0.8, max_search_time=30)



def start_tests():
    print("--- TEST STARTED ---")

    time.sleep(5)
    sik.tap(Key.f5)

    create_level_test()
    publish_level_test()
    sequence_creation_test()
    component_creation_test()
    
    sik.hotkey(Key.alt, Key.f4)

    print("--- TEST ENDED ---")

def create_level_test():
    failed = False

    try:
        sik.click("img/CreateNewButton.jpg", precision=0.8, max_search_time=15)
        sik.wait("img/NewLevelButton.jpg", precision=0.7, max_search_time=15)
    except Exception:
        failed = True
        print("Create Level Test - FAILED")
    
    if not failed:
        print("Create Level Test - PASSED")


def publish_level_test():
    failed = False

    try:
        sik.click("img/NewLevelButton.jpg", precision=0.7, max_search_time=15)
        sik.click("img/PublishButton.jpg", precision=0.7, max_search_time=15)
        sik.click("img/DownloadLevelsButton.jpg", precision=0.7, max_search_time=15)
        sik.wait("img/DownloadedLevelsVerification.jpg", precision=0.7, max_search_time=30)
        time.sleep(1)
        sik.click("img/BackButton.jpg", precision=0.76, max_search_time=30)
    except Exception:
        failed = True
        print("Publish Level Test - FAILED")
    
    if not failed:
        print("Publish Level Test - PASSED")

def sequence_creation_test():
    failed = False

    try:
        sik.click("img/NewLevelButton.jpg", precision=0.7, max_search_time=15)
        sik.click("img/EditButton.jpg", precision=0.7, max_search_time=15)
        sik.click("img/TemplatesButton.jpg", precision=0.7, max_search_time=15)
        sik.dragDrop(start_location=(900,475), destination_loc=(1300,600), speed=1)
        sik.wait("img/SequenceButton.jpg", precision=0.7, max_search_time=15)
    except Exception:
        failed = True
        print("Sequence Level Test- FAILED")
    
    if not failed:
        print("Sequence Level Test- PASSED")

def component_creation_test():
    failed = False

    try:
        sik.click("img/SequenceButton.jpg", precision=0.7, max_search_time=15)
        sik.click("img/SequencePlusButton.jpg", precision=0.7, max_search_time=15)
        sik.click("img/SequenceCreateNewBulletButton.jpg", precision=0.7, max_search_time=15)
        sik.wait("img/SequenceBulletVerification.jpg", precision=0.7, max_search_time=15)
    except Exception:
        failed = True
        print("Component Creation Test - FAILED")
    
    if not failed:
        print("Component Creation Test - PASSED")

if __name__ == "__main__":
    start_tests()
