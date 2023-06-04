# Data Validation with Python

- All examples are tested with Python 3.9.11.
- Each separate section has its own `requirements.txt` file, and all requirements files are linked in the main `requirements.txt` at the root of the repository.


## When to use what

- Use Pydantic for non-Django projects
- Use Django forms/model-forms for Django projects when working with HTML forms or other type of input e.g. (file uploads, messaged etc.)
- Use DRF Serializers for Django projects when building REST APIs
- Use JsonSchema to ensure schema compatibility when 3rd party APIs are involved


---


**Disclaimer:** All code is intended for educational purposes only and not intended to be used in production.  The code is not optimized and may not be the best way to implement the functionality.  The code is not guaranteed to be correct and is provided as-is with no warranty.  All code is subject to change without notice.
