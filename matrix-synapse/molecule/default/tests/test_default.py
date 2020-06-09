"""Role testing files using testinfra."""

def test_matrix_reachable(host):
    cmd = host.run("curl localhost:8008 -L")
    assert cmd.succeeded
    assert 'WordPress installation process' in cmd.stdout
    

def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
