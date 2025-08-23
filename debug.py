try:
    from flask_sqlalchemy import SQLAlchemy
except Exception as e:
    import sys
    print("DEBUG: Import error ->", e, file=sys.stderr)
    raise
