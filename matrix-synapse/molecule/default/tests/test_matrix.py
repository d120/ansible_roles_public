"""Role testing files using testinfra."""

def test_matrix_reachable(host):
    cmd = host.run("curl localhost:8008/_matrix/static/ -L")
    assert cmd.succeeded
    assert 'It works! Synapse is running' in cmd.stdout
    
def test_matrix_service(host):
    service = host.service("matrix-synapse")
    assert service.is_running
    assert service.is_enabled
