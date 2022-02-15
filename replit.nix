{ pkgs }:
let

    nginxModified = pkgs.nginx.overrideAttrs (oldAttrs: rec {
        configureFlags = oldAttrs.configureFlags ++ [
            "--http-client-body-temp-path=/home/runner/IA2/cache/client_body"
            "--http-proxy-temp-path=/home/runner/IA2/cache/proxy"
            "--http-fastcgi-temp-path=/home/runner/IA2/cache/fastcgi"
            "--http-uwsgi-temp-path=/home/runner/IA2/cache/uwsgi"
            "--http-scgi-temp-path=/home/runner/IA2/cache/scgi"
         ];
    });

in {
    deps = [
        nginxModified
        pkgs.nodePackages.vue-cli
        pkgs.nodePackages.yarn
        pkgs.python39
        pkgs.python39Packages.flask
        pkgs.python39Packages.waitress
        pkgs.jupyter
    ];

}