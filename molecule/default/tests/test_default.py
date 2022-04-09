"""Role testing files using testinfra."""


def test_chrony_installed(host):
    pkg = host.package("chrony")
    assert pkg.is_installed


def test_chrony_config_file(host):
    f = host.file("/etc/chrony/chrony.conf")
    assert f.exists
    assert f.contains("nl.pool.ntp.org")
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644


def test_chrony_running_and_enabled(host):
    servicename = host.service("chrony")
    assert servicename.is_running
    assert servicename.is_enabled
