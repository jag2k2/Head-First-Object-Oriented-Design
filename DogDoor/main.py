from threading import Timer


class DogDoor:
    _open: bool

    def __init__(self):
        self._open = False

    def open(self) -> None:
        print("The dog door opens.")
        self._open = True

    def close(self) -> None:
        print("The dog door closes.")
        self._open = False

    def is_open(self) -> bool:
        return self._open


class Remote:
    _door: DogDoor

    def __init__(self, door: DogDoor):
        self._door = door

    def press_button(self) -> None:
        print("Pressing the remote control button...")
        if self._door.is_open():
            self._door.close()
        else:
            self._door.open()
            timer: Timer = Timer(5, self._door.close)
            timer.start()


door: DogDoor = DogDoor()
remote: Remote = Remote(door)
print("Fido barks to go outside...")
remote.press_button()
print("\nFido has gone outside")
print("Fido's all done")
print("Fido's back inside\n")

