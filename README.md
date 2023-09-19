# Info
This spec was tested with PhotonOS 5.0 GA only, hasn't tried with 4.0, however it should be a repeatable step

# Pre-requisites
## User
Should be root to perform the below steps to make it simpler

## OS
Photon OS 5.0 GA

## Initial Setup
Install wget 
```
tdnf install wget
```
Install git 
```
tdnf install git
```

# Build
Create a folder where you want to do this build and within it, pull down photon repository 
```
git clone https://github.com/vmware/photon.git
```
Pull down this repo
```
git clone https://github.com/snapshotleisure/photon-os-qemu-guest-agent.git
```
Run Script
```
./photon/tools/scripts/build_spec.sh ./photon-os-qemu-guest-agent/src/qemu-guest-agent.spec ./photon-os-qemu-guest-agent/binaries
```
# Install
Install the rpm
```
tdnf install ./photon-os-qemu-guest-agent/binaries/RPMS/x86_64/qemu-guest-agent-8.1.0-1.ph5.x86_64.rpm
```
Create Service
```
cat > /etc/systemd/system/qemu-guest-agent.service << EOF
[Unit]
Description=QEMU Guest Agent
BindsTo=dev-virtio\x2dports-org.qemu.guest_agent.0.device
After=dev-virtio\x2dports-org.qemu.guest_agent.0.device

[Service]
ExecStart=-/usr/bin/qemu-ga
Restart=always
RestartSec=0

[Install]
WantedBy=multi-user.target
EOF
```
Enable and start the service
```
systemctl enable qemu-guest-agent
systemctl start qemu-guest-agent
```