from setuptools import find_packages, setup


def read(f):
    return open(f, encoding="utf-8").read()


setup(
    name="drf-hcaptcha",
    version="1.0.1",
    description="Django rest framework hcaptcha field serializer.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Alexander I",
    author_email="sasha.2000ibr@gmail.com",
    license="MIT",
    url="https://github.com/pysashapy/drf-hcaptcha",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "django>=3.1",
        "djangorestframework>=3.11",
        "django-ipware>=2.1",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-django", "pytest-cov", "pytest-mock"],
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "django",
        "drf",
        "rest",
        "django-rest-framework",
        "hCAPTCHA",
        "hCAPTCHA v2",
        "hCAPTCHA v3",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Framework :: Django",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
