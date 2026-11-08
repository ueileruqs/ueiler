#!/usr/bin/env python3
"""Start the existing AISWEB app in a GitHub Codespaces container."""
import http.server
import os
import runpy
import webbrowser
from pathlib import Path


class CodespacesHTTPServer(http.server.ThreadingHTTPServer):
    """Expose the app on the container interface for Codespaces port forwarding."""

    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
        _, port = server_address
        port = int(os.environ.get("PORT", port))
        super().__init__(("0.0.0.0", port), RequestHandlerClass, bind_and_activate)


# The original script imports ThreadingHTTPServer and opens a browser on the
# container. Replace these behaviors before executing it as the main program.
http.server.ThreadingHTTPServer = CodespacesHTTPServer
webbrowser.open = lambda *args, **kwargs: False

app = Path(__file__).resolve().parent.parent / "ais"
runpy.run_path(str(app), run_name="__main__")
