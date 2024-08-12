#!/bin/bash

cd ..
git add .
echo 'Mensagem do commit: '
read message
git commit -am "$message"
git push
git push blogrepo
ssh rarorza@rarorza.site \
  'git -C /home/rarorza/blogapp/ ' \
  'pull blogrepo main && ' \
  'sudo systemctl restart blog && sudo systemctl restart nginx'
