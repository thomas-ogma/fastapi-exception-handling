# fastapi-exception-handling

Note: `.env` is there in the repo itself as it does not contain any credentials & anyone can quickly get up & running.

We should only raise (throw) exceptions from controllers and let the global error/exception handler catch the error. It's not just limited to FastAPI but applies to all the server-side frameworks e.g. .NET, Express, etc. Adding try/catch to every controller leads to code bloat. The last time Tanmay asked the same question, I asked him to use global validation and exception handlers provided by FastAPI. You can have HTTPException, RequestValidationError, SQLAlchemyException, Exception (generic), etc.
 
Another approach you can take is to use middleware to catch different types of errors. If you choose the middleware approach, you won't need the exception handlers. So, the choice is up to your preferences!
 
FastAPI already provides lots of good examples:
https://fastapi.tiangolo.com/tutorial/handling-errors/
https://fastapi.tiangolo.com/tutorial/middleware/
 
For the logging, you can go with Rajib Gupta's suggestion. Once you have created the logger, you can use it directly in the controller or anywhere you need or create a custom logger to log automatically. Check the functools module and wrap function (if you go with custom decorator)
 
You should also consider logging the requests using the default log_config param (if not already) 
 
You can find lots of good opinions here: https://github.com/tiangolo/fastapi/discussions/7457


Here's the main crux of the code (in main.py):
```
    # Step 1: Create a logging instance
    logger = logging.getLogger(__name__)


    # Step 2: We can either handle a specific exception, here for example "ZeroDivisionError"
    @app.exception_handler(ZeroDivisionError)
    async def zerodivision_exception_handler(request, exc):
        logger.exception(exc)
        return JSONResponse(status_code=500, content={"error": str(exc)})

    #         We can also handle all exceptions in one place, using the 'Exception' superclass.
    @app.exception_handler(Exception)
    async def validation_exception_handler(request, exc):
        logger.exception(exc)
        return JSONResponse(status_code=500, content={"error": str(exc)})

```

