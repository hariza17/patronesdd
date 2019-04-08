from observer.Subject import Subject
from observer.ConcreteObserver import ConcreteObserver


def main():
    subject = Subject()
    concrete_observer = ConcreteObserver()
    subject.attach(concrete_observer)

    subject.subject_state = 123123
    subject.subject_state = 2
    subject.subject_state = 4


if __name__ == '__main__':
    main()
