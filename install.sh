if [ "$EUID" -ne 0 ]; then
  echo "Please run the installer as root"
  exit
fi

echo "Installing UPS Notify..."

echo "Copying service script"

cp ups-notify.service /etc/systemd/system/ 2>/dev/null

echo "Reloading systemd"

systemctl daemon-reload 2>/dev/null

echo "Enabling and starting service"

systemctl enable ups-notify 2>/dev/null
systemctl start ups-notify 2>/dev/null

echo "Installation complete."