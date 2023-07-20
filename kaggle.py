# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2023-06-20T10:24:14.891542Z","iopub.execute_input":"2023-06-20T10:24:14.892176Z","iopub.status.idle":"2023-06-20T10:24:16.099428Z","shell.execute_reply.started":"2023-06-20T10:24:14.892148Z","shell.execute_reply":"2023-06-20T10:24:16.098152Z"}}
# Проверяем наличие видеокарты в блокноте

!nvidia-smi

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2023-06-20T10:24:20.620875Z","iopub.execute_input":"2023-06-20T10:24:20.621234Z","iopub.status.idle":"2023-06-20T10:24:21.598461Z","shell.execute_reply.started":"2023-06-20T10:24:20.621201Z","shell.execute_reply":"2023-06-20T10:24:21.597215Z"}}
# Проверяем версию Python

!/opt/conda/bin/python --version

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2023-06-20T16:28:13.223526Z","iopub.execute_input":"2023-06-20T16:28:13.223789Z","iopub.status.idle":"2023-06-20T16:29:25.837433Z","shell.execute_reply.started":"2023-06-20T16:28:13.223765Z","shell.execute_reply":"2023-06-20T16:29:25.836226Z"}}
# Установка зависимостей

!pip install -U --no-warn-script-location so-vits-svc-fork > /dev/null
!cd /kaggle/working > /dev/null

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2023-06-20T16:29:27.910394Z","iopub.execute_input":"2023-06-20T16:29:27.910790Z","iopub.status.idle":"2023-06-20T16:29:35.301279Z","shell.execute_reply.started":"2023-06-20T16:29:27.910750Z","shell.execute_reply":"2023-06-20T16:29:35.299881Z"}}
!mkdir -p "dataset_raw_raw"
!mkdir -p "dataset_raw"
!rm -r "dataset"
!cp -R /kaggle/input/!!!НАЗВАНИЕ ДАТАСЕТА!!!/ -t "dataset_raw_raw/"

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2023-06-20T16:31:03.506181Z","iopub.execute_input":"2023-06-20T16:31:03.506697Z","iopub.status.idle":"2023-06-20T16:34:26.667527Z","shell.execute_reply.started":"2023-06-20T16:31:03.506659Z","shell.execute_reply":"2023-06-20T16:34:26.666399Z"}}
# Предобработка датасета (скипнуть если уже выполнили)

!svc pre-resample -i "dataset_raw_raw/"
!svc pre-config
!svc pre-hubert

# %% [code] {"scrolled":true,"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2023-06-20T16:34:32.859915Z","iopub.execute_input":"2023-06-20T16:34:32.860979Z","iopub.status.idle":"2023-06-20T16:36:00.814913Z","shell.execute_reply.started":"2023-06-20T16:34:32.860940Z","shell.execute_reply":"2023-06-20T16:36:00.813659Z"}}
# Запуск тренировки

!svc train --model-path logs/44k

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2023-06-20T16:36:19.144231Z","iopub.execute_input":"2023-06-20T16:36:19.144611Z","iopub.status.idle":"2023-06-20T16:39:48.284220Z","shell.execute_reply.started":"2023-06-20T16:36:19.144578Z","shell.execute_reply":"2023-06-20T16:39:48.283011Z"}}
!zip -r logs.zip logs/
from IPython.display import FileLink

FileLink(r'logs.zip')