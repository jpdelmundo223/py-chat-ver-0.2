from setuptools import setup
from setuptools import find_packages

install_requires = [
    "flask",
    "flask-socketio",
    "flask-sqlalchemy",
    "flask-login",
    "flask-migrate",
    "flask-wtf",
    "email-validator",
    "eventlet"
]

setup(
    name="pyChat",
    version="0.2",
    description="A real-time chat application developed using flask microframework and flask-socketio.",
    packages=find_packages(),
    author="John Paul Del Mundo",
    author_email="jpdelmundo223@gmail.com",
    license="MIT",
    requires=install_requires
)