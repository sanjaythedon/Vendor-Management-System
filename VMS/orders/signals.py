from django import dispatch


class UpdateSignalSender:
    acknowledge_update = dispatch.Signal()

    @classmethod
    def send_signal(cls):
        cls.acknowledge_update.send(sender=cls, name="Sanjay", age=22)