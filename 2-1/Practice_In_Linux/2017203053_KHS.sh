#!/bin/bash

function permission_message(){
    echo '                             _   _  _____'
    echo '                            | \ | ||  _  |'
    echo '                            |  \| || | | |'
    echo '                            |     || | | |'
    echo '                            | |\  |\ \_/ /'
    echo '                            \_| \_/ \___/'
    echo ''
    echo ''
    echo '  ______  _____ ______ ___  ___ _____  _____  _____  _____  _____  _   _'
    echo ' |__ _ \ |  ___|| ___ \|  \/  ||_   _|/  ___|/  ___||_   _||  _  || \ | |'
    echo ' | |_/ / | |__  | |_/ /| .  . |  | |  \ `--. \ `--.   | |  | | | ||  \| |'
    echo ' | _ _/  |  __| |    / | |\/| |  | |   `--. \ `--. \  | |  | | | || .   |'
    echo ' | |     | |___ | |\ \ | |  | | _| |_ /\__/ //\__/ / _| |_ \ \_/ /| |\  |'
    echo ' \_|     \____/ \_| \_|\_|  |_/ \___/ \____/ \____/  \___/  \___/ \_| \_/'
    echo ""
    echo ""
    echo "If you want to go back , Please Type 'q' or 'Q'"
    
}

userid=`cut -f1 -d: /etc/passwd | sort` # user id 정렬
declare -a useridarr=($userid) # user id 배열 형태로 저장


declare -i uidcursor=16
declare -i infocursor=16
L_R_check=0 # 0이 왼쪽 1이 오른쪽
id_U_D_check=20 # up = +1 down = -1
info_U_D_check=0 # up = +1 down = -1
declare -i idrow # 현재user 커서가 위치한 행
declare -i inforow # 현재 info 커서가 위치한 행
declare -i temp_id_row # 현재 커서가 위치한 user의 정보를 저장하기위한 임시 변수
declare -i j # 해당 user의 프로세스 목록을 출력하기 위한 변수
declare -i key_check=0 # 키 입력에서 이상한 입력을 받았을 시 에러메시지 출력을 위한 변수
declare -i skey_check=0 # q 다음 엔터 입력 유무 확인용
declare -i id_array_length # 현재 컴퓨터의 user 수
declare -i info_array_length=1 # user의 프로세스 수
id_array_length=${#useridarr[*]}
declare -i temp_array_length=$id_array_length
declare -i k=0 # scroll uid
declare -i t=0 # scroll process info
declare -i stat_check=1
declare -i cursor_current_pid

current_userid=`whoami`
declare -a killed_process_list_userid
declare -a killed_process_list_usercmd
declare -a killed_process_list_userpid
declare -a killed_process_list_userstime
declare -i k_p_l_idx=0

if  [[ $id_array_length -gt 20 ]] 
then
    id_array_length=20
fi


while :
do
    
   clear
echo "______                     _    _"
echo "| ___ \                   | |  (_)"
echo "| |_/ / _ __   __ _   ___ | |_  _   ___   ___"
echo "|  __/ |  __| / _  | / __|| __|| | / __| / _ \\"
echo "| |    | |   | (_| || (__ | |_ | || (__ |  __/"
echo "\\_|    |_|    \__,_| \\___| \\__||_| \\___| \\___|"
echo ""
echo "(_)       | |    (_)"
echo " _  _ __  | |     _  _ __   _   _ __  __"
echo "| ||  _ \ | |    | ||  _ \ | | | |\ \/ /"
echo "| || | | || |____| || | | || |_| | >  <"
echo "|_||_| |_|\\_____/|_||_| |_| \\__,_|/_/\\_\\"
echo ""
echo "-NAME-----------------CMD--------------------PID-----STIME------"


    if [[ $info_array_length -gt 20 ]] # 커서의 이동 범위 설정
    then
        info_array_length=20
    fi
    if [[ $id_U_D_check -gt 20 ]]
    then
        id_U_D_check=20
        k=`expr $k - 1 `
        if [[ $k -lt 0 ]]
        then
            k=0
        fi

    elif [[ $id_U_D_check -lt ` expr 21 - $id_array_length ` ]]
    then
        id_U_D_check=` expr 21 - $id_array_length `
        k=`expr $k + 1`
        if [[ $k -gt `expr $temp_array_length - 20 ` ]]
        then
            k=`expr $temp_array_length - 20`
        fi
    fi
    if [[ $info_U_D_check -gt 0 ]] # 위쪽
    then
        info_U_D_check=0
        if [[ $temp_info_length -gt 20 ]]
        then
        t=`expr $t - 1 `
        if [[ $t -lt 0 ]]
        then
            t=0
        fi
        fi
    fi
    if [[ $info_U_D_check -lt `expr 1 - $info_array_length ` ]] # 아래쪽
    then
        info_U_D_check=`expr 1 - $info_array_length `
        if [[ $temp_info_length -gt 20 ]]
        then
        t=`expr $t + 1 `
        if [[ $t -gt `expr $temp_info_length - 20` ]]
        then
            t=`expr $temp_info_length - 20`
        fi
        fi
    fi

    idrow=` expr $uidcursor - $id_U_D_check + 20  ` 
    inforow=` expr $infocursor - $info_U_D_check `
    temp_id_row=`expr $idrow - 16 `

     
    usercmd=`ps -ef | grep ^${useridarr[$temp_id_row+k]} | sort -u -n -k 2,2 -r | awk '{print $8}'`
    declare -a usercmdarr=($usercmd)
    userpid=`ps -ef | grep ^${useridarr[$temp_id_row+k]} | sort -u -n -k 2,2 -r | awk '{print $2}' `
    declare -a userpidarr=($userpid)
    userstime=`ps -ef | grep ^${useridarr[$temp_id_row+k]} | sort -u -n -k 2,2 -r | awk '{print $5}' `
    declare -a userstimearr=($userstime)
    info_array_length=${#usercmdarr[*]}
    temp_info_length=$info_array_length
    current_process_stat=`ps -faux | grep ^${useridarr[$temp_id_row+k]} | sort -u -n -k 2,2 -r | awk '{print $2" "$8}'| grep +$ `
    declare -a current_process_fg_list=($current_process_stat)
    process_length=${#current_process_fg_list[*]}
    
    loop_condition=`expr $process_length / 2`
    if [[ $info_array_length = 0 ]] 
    then
    L_R_check=0
    fi
    j=0
    for (( i = 0 ; i < 20 ; i++ )) # 20줄 출력
    do 
         
        stat_check=1
        for (( p=0 ; p < $loop_condition ; p++ ))
        do
# v=`expr 2 \* $p`
            if [[ ${current_process_fg_list[2*p]} = ${userpidarr[i+k]} ]]
            then
                stat_check=0
            fi
        done

        if [[ $L_R_check = 0 ]] # 커서가 user목록에서 이동 
        then
            
        
            info_U_D_check=0
            if [[ $idrow = ` expr 16 + $i ` ]]
            then 
               
                printf "%c[41m%20.20s[0m%c" "|" ${useridarr[i+k]} "|"
                if [[ $info_array_length != 0 && ${usercmdarr[i]} != "" && $stat_check = 1 ]] 
                then
                    printf "B %-20.20s%c%7.7s%c%9.9s %c\n" ${usercmdarr[i]} "|" ${userpidarr[i]} "|" ${userstimearr[i]} "|"
                elif [[ $info_array_length != 0 && $stat_check = 0 ]]
                then
                    printf "F %-20.20s%c%7.7s%c%9.9s %c\n" ${usercmdarr[i]} "|" ${userpidarr[i]} "|" ${userstimearr[i]} "|"

                else
                printf "%-22.22s%c%7.7s%c%9.9s %c\n" " " "|" " " "|" " " "|"
                fi


            else
                printf "[0m%c%20.20s%c" "|" ${useridarr[i+k]} "|"
                
                if [[ $info_array_length != 0 && ${usercmdarr[i]} != "" && $stat_check = 1 ]]
                then
                    printf "B %-20.20s%c%7.7s%c%9.9s %c\n" ${usercmdarr[i]} "|" ${userpidarr[i]} "|" ${userstimearr[i]} "|"

                elif [[ $info_array_length != 0 && $stat_check = 0 ]] 
                then
                    printf "F %-20.20s%c%7.7s%c%9.9s %c\n" ${usercmdarr[i]} "|" ${userpidarr[i]} "|" ${userstimearr[i]} "|"
                else
                printf "%-22.22s%c%7.7s%c%9.9s %c\n" " " "|" " " "|" " " "|"
                fi

            fi
            
        fi

        if [[ $L_R_check = 1 ]] # 커서가 info 목록에서 이동 시
        then
            
            printf "[0m%c" "|"
           
            if [[ $j = $temp_id_row ]] # 현재 user커서가 가리키는 user
            then
                printf "[41m%20s[0m%c" ${useridarr[j+k]} "|"

                cursor_current_userid=${useridarr[j+k]}
            else
                printf "[0m%20s%c" ${useridarr[j+k]} "|"
            fi

 
            if [[ $inforow = ` expr $infocursor + $j ` ]] # 현재 user커서가 가리키는 user의 정보 출력
            then
                if [[ $info_array_length != 0 && ${usercmdarr[i]} != "" &&  $stat_check = 1 ]] 
                then
                    printf "[42mB %-20.20s%c%7s%c%9.9s[0m %c\n" ${usercmdarr[j+t]} "|" ${userpidarr[j+t]} "|" ${userstimearr[j+t]} "|"
                    current_cmd=${usercmdarr[j+t]}
                    current_pid=${userpidarr[j+t]}
                    current_stime=${userstimearr[j+t]}


                elif [[ $info_array_length != 0 && $stat_check = 0 ]]
                then
                    printf "[42mF %-20.20s%c%7s%c%9.9s[0m %c\n" ${usercmdarr[j+t]} "|" ${userpidarr[j+t]} "|" ${userstimearr[j+t]} "|"
                    current_cmd=${usercmdarr[j+t]}
                    current_pid=${userpidarr[j+t]}
                    current_stime=${userstimearr[j+t]}


                else
                printf "%-22.22s%c%8.7s%c%9.9s %c\n" " " "|" " " "|" " " "|"
                fi


            else
                if [[ $info_array_length != 0 && ${usercmdarr[i]} != "" &&  $stat_check = 1 ]]
                then
                    printf "B [0m%-20.20s%c%7s%c%9.9s %c\n" ${usercmdarr[j+t]} "|" ${userpidarr[j+t]} "|" ${userstimearr[j+t]} "|"

                elif [[ $info_array_length != 0 && $stat_check = 0 ]]
                then
                    printf "F [0m%-20.20s%c%7s%c%9.9s %c\n" ${usercmdarr[j+t]} "|" ${userpidarr[j+t]} "|" ${userstimearr[j+t]} "|"

                else

                    printf "[0m%-22.22s%c%7s%c%9.9s %c\n" " " "|" " " "|" " " "|"
                fi

                

            fi
            j=` expr $j + 1 `


        fi
    done
    
    echo "----------------------------------------------------------------" # 프롬프트
    echo "If you want to exit , Please Type 'q' or 'Q'"
    echo "If you want to see killed process list, Please Type 'l' or 'L"
    
    key_check=0
    skey_check=0
    nkey_check=0
    lkey_check=0
    sleep 3& 
    sleep_info=`ps -ef | grep ^${useridarr[$temp_id_row+k]} | pgrep -n 'sleep'`
    read -t 3 -n 1 key # 3초간 키 하나 입력받음
    
    if [[ $L_R_check = 1 && $key = "" && `jobs -l | grep 'sleep 3 &'` != "" ]] 
    then
        
        if [[ $current_userid = $cursor_current_userid || $current_userid = root ]]
        then
            kill -9 $current_pid
            killed_process_list_userid[$k_p_l_idx]=$current_userid
            killed_process_list_usercmd[$k_p_l_idx]=$current_cmd
            killed_process_list_userpid[$k_p_l_idx]=$current_pid
            killed_process_list_userstime[$k_p_l_idx]=$current_stime
            k_p_l_idx=`expr $k_p_l_idx + 1`

        else
            clear
            permission_message
            while [ $nkey_check = 0 ]
            do
                read -n 2 nkey
                if [[ $nkey = "q" || $nkey = "Q" ]]
                then
                    nkey_check=1
                fi
            done
            

        fi    
    fi
    
    if [[ $key = "q" || $key = "Q" ]]
    then
        read -n 1 skey
        
        if [[ $skey = "" ]]
        then
            exit
        fi
    elif [[ $key = "L" || $key = "l" ]]
    then
        read -n 1 mkey
        if [[ $mkey = "" ]]
        then
        
        clear
        printf "The list of killed processes information\n"
        echo "-NAME-----------------CMD--------------------PID-----STIME------"
        for(( l=0 ; l<$k_p_l_idx ; l++))
        do
            printf "|%20s|%-22.22s|%7s|%9.9s |\n" ${killed_process_list_userid[l]} ${killed_process_list_usercmd[l]} ${killed_process_list_userpid[l]} ${killed_process_list_userstime[l]}

            
        done
        echo "----------------------------------------------------------------" # 프롬프트
        echo "If you want to exit , Please Type 'q' or 'Q'"

        while [ $lkey_check = 0 ]
        do
            read -n 2 lkey
            if [[ $lkey = "q" || $lkey = "Q" ]]
            then
                lkey_check=1
                fi
        done
        
        fi
    elif [[ $L_R_check = 0 && $key = A ]] 
    then
    id_U_D_check=` expr $id_U_D_check + 1 `
    elif [[ $L_R_check = 1 && $key = A ]]
    then
    info_U_D_check=` expr $info_U_D_check + 1 `
    
    elif [[ $L_R_check = 0 && $key = B ]]
    then
    id_U_D_check=` expr $id_U_D_check - 1 `
    elif [[ $L_R_check = 1 && $key = B ]]
    then
    info_U_D_check=` expr $info_U_D_check - 1 `
    elif [[ $L_R_check = 0 && $key = C ]]
    then 
    L_R_check=1
    
    elif [[ $L_R_check = 1 && $key = D ]]
    then
    L_R_check=0
    t=0
    elif [[ $key = "" ]]
    then
        key_check=0
    fi
    kill -9 $sleep_info
    clear
done

