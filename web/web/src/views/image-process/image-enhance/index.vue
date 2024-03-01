<script setup>
import { ref } from 'vue'
import { NButton, NForm, NFormItem, NInput, NTabPane, NTabs, NImage } from 'naive-ui'
import { useI18n } from 'vue-i18n'
import CommonPage from '@/components/page/CommonPage.vue'
import { useUserStore } from '@/store'
import api from '@/api'
import { is } from '~/src/utils'

const { t } = useI18n()
const userStore = useUserStore()
const isLoading = ref(false)

// 图像亮度信息窗口
const infoForm = ref({
  inputPath: 'D:\\work_record\\1031',
  outputPath: '',
  brightnessFactor: '2',
});
const infoFormRules = {
  inputPath: [
    { required: true, message: "请输入输入路径！", trigger: 'blur' },
  ],
  outputPath: [
    { required: false, message: "请输入输出路径！", trigger: 'blur' },
  ],
  brightnessFactor: [
    { required: true, message: "请输入亮度因子！", trigger: 'blur' },
  ],
};

const handleConfirm = () => {
  const data = {
    inputPath: infoForm.value.inputPath,
    outputPath: infoForm.value.outputPath,
    brightnessFactor: infoForm.value.brightnessFactor,
    name: userStore.name
  };

//   api.imageEnhance(data)
//     .then(response => {
//       console.log(response)
//       // if (response.message === 'OK') {
//       //   console.info("图像处理成功！消息：" + response.message);
//       // } else {
//       //   console.error("图像处理失败！消息：" + response.message);
//       // }
//     })
//     .catch(res => {
//       console.info("发生错误！", res);
//     });
// };

api.imageEnhance(data)
.then((response) => {
      console.log(response)
      // if (response.message === 'OK') {
      //   console.info("图像处理成功！消息：" + response.message);
      // } else {
      //   console.error("图像处理失败！消息：" + response.message);
      // }
    })
  .catch(error => {
    console.log("发生错误！", error);
  });
console.log('Promise调用完成');
};

</script>


<template>
  <CommonPage :show-header="false">
    <NTabs type="line" animated>
      <NTabPane name="website" :tab="$t('views.image.label_modify_information')">
        <div class="m-30 flex items-center">
          <NForm
            ref="infoFormRef"
            label-placement="left"
            label-align="left"
            label-width="100"
            :model="infoForm"
            :rules="infoFormRules"
            class="w-400"
          >
            <NFormItem :label="'输入路径'" path="inputPath">
              <NInput
                v-model:value="infoForm.inputPath"
                type="text"
                :placeholder="'请输入输入路径'"
              />
            </NFormItem>
            <NFormItem :label="'输出路径'" path="outputPath">
              <NInput
                v-model:value="infoForm.outputPath"
                type="text"
                :placeholder="'请输入输出路径'"
              />
            </NFormItem>
            <NFormItem :label="'亮度因子'" path="brightnessFactor">
              <NInput
                v-model:value="infoForm.brightnessFactor"
                type="text"
                :placeholder="'请输入亮度因子'"
              />
            </NFormItem>
            <NButton type="primary" :loading="isLoading" @click="handleConfirm">
              {{ $t('common.buttons.confirm') }}
            </NButton>
          </NForm>
        </div>
      </NTabPane>
    </NTabs>
  </CommonPage>
</template>
