import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

