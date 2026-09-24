<template>
  <div id="app">
    <div class="form-card">
      <h2>用户信息登记</h2>

      <!-- 姓名 -->
      <div class="field">
        <label>姓名</label>
        <input 
          type="text" 
          v-model="form.name" 
          placeholder="请输入姓名（至少2个字符）"
          @blur="validateName"
        />
        <span v-if="errors.name" class="error">{{ errors.name }}</span>
      </div>

      <!-- 邮箱 -->
      <div class="field">
        <label>邮箱</label>
        <input 
          type="email" 
          v-model="form.email" 
          placeholder="请输入有效的邮箱地址"
          @input="validateEmail"
        />
        <span v-if="errors.email" class="error">{{ errors.email }}</span>
      </div>

      <!-- 密码 -->
      <div class="field">
        <label>密码</label>
        <input 
          type="password" 
          v-model="form.password" 
          placeholder="至少6位，包含字母和数字"
          @input="validatePassword"
        />
        <!-- 密码强度指示条 -->
        <div class="strength-bar">
          <div 
            class="strength-fill" 
            :style="{ width: passwordStrength + '%', background: strengthColor }"
          ></div>
        </div>
        <span v-if="errors.password" class="error">{{ errors.password }}</span>
      </div>

      <!-- 确认密码 -->
      <div class="field">
        <label>确认密码</label>
        <input 
          type="password" 
          v-model="form.confirmPassword" 
          placeholder="再次输入密码"
          @input="validateConfirm"
        />
        <span v-if="errors.confirm" class="error">{{ errors.confirm }}</span>
      </div>

      <!-- 提交按钮 -->
      <button 
        class="submit-btn" 
        :disabled="!isFormValid"
        @click="submitForm"
      >
        {{ isFormValid ? '提交登记' : '请完善信息' }}
      </button>

      <!-- 提交成功反馈 -->
      <div v-if="submitted" class="success-message">
        登记成功！感谢您的注册。
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        name: '',
        email: '',
        password: '',
        confirmPassword: ''
      },
      errors: {
        name: '',
        email: '',
        password: '',
        confirm: ''
      },
      submitted: false
    }
  },
  computed: {
    // 密码强度（0-100）
    passwordStrength() {
      const pwd = this.form.password
      if (!pwd) return 0
      let score = 0
      if (pwd.length >= 6) score += 20
      if (pwd.length >= 8) score += 20
      if (/[A-Z]/.test(pwd)) score += 20
      if (/[0-9]/.test(pwd)) score += 20
      if (/[^A-Za-z0-9]/.test(pwd)) score += 20
      return Math.min(score, 100)
    },
    strengthColor() {
      const s = this.passwordStrength
      if (s < 40) return '#e74c3c'
      if (s < 70) return '#f39c12'
      return '#2ecc71'
    },
    // 表单整体是否有效（所有字段无错误且非空）
    isFormValid() {
      return (
        this.form.name.trim().length >= 2 &&
        this.form.email.length > 0 &&
        !this.errors.email &&
        this.form.password.length >= 6 &&
        this.form.confirmPassword === this.form.password &&
        this.form.confirmPassword.length > 0
      )
    }
  },
  methods: {
    validateName() {
      const val = this.form.name.trim()
      if (val.length === 0) {
        this.errors.name = '姓名不能为空'
      } else if (val.length < 2) {
        this.errors.name = '姓名至少2个字符'
      } else {
        this.errors.name = ''
      }
    },
    validateEmail() {
      const email = this.form.email
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+(\.[^\s@]+)*$/
      if (email.length === 0) {
        this.errors.email = '邮箱不能为空'
      } else if (!re.test(email)) {
        this.errors.email = '请输入正确的邮箱格式'
      } else {
        this.errors.email = ''
      }
    },
    validatePassword() {
      const pwd = this.form.password
      if (pwd.length === 0) {
        this.errors.password = '密码不能为空'
      } else if (pwd.length < 6) {
        this.errors.password = '密码至少6位'
      } else if (!/[a-zA-Z]/.test(pwd) || !/[0-9]/.test(pwd)) {
        this.errors.password = '密码需包含字母和数字'
      } else {
        this.errors.password = ''
      }
      // 每次修改密码时，重新校验确认密码
      if (this.form.confirmPassword) {
        this.validateConfirm()
      }
    },
    validateConfirm() {
      if (this.form.confirmPassword !== this.form.password) {
        this.errors.confirm = '两次密码输入不一致'
      } else {
        this.errors.confirm = ''
      }
    },
    submitForm() {
      // 模拟提交（实际开发中可调用 API）
      this.submitted = true
      setTimeout(() => {
        this.submitted = false
        // 可重置表单
        // this.form = { name: '', email: '', password: '', confirmPassword: '' }
        // this.errors = { name: '', email: '', password: '', confirm: '' }
      }, 3000)
    }
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  font-family: 'Segoe UI', '微软雅黑', sans-serif;
  background: #f0f2f5;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
#app {
  width: 100%;
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.form-card {
  background: white;
  border-radius: 16px;
  padding: 32px 28px;
  max-width: 480px;
  width: 100%;
  box-shadow: 0 8px 30px rgba(0,0,0,0.08);
}
h2 {
  text-align: center;
  margin-bottom: 28px;
  color: #2c3e50;
  font-weight: 600;
  font-size: 24px;
}
.field {
  margin-bottom: 20px;
}
label {
  display: block;
  font-weight: 500;
  font-size: 14px;
  color: #34495e;
  margin-bottom: 4px;
}
input {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #dce1e6;
  border-radius: 8px;
  font-size: 15px;
  transition: border 0.2s;
}
input:focus {
  border-color: #42b883;
  outline: none;
  box-shadow: 0 0 0 3px rgba(66, 184, 131, 0.15);
}
.error {
  font-size: 13px;
  color: #e74c3c;
  margin-top: 4px;
  display: block;
}
.strength-bar {
  width: 100%;
  height: 4px;
  background: #ecf0f1;
  border-radius: 4px;
  margin-top: 8px;
  overflow: hidden;
}
.strength-fill {
  height: 100%;
  transition: width 0.3s, background 0.3s;
  border-radius: 4px;
}
.submit-btn {
  width: 100%;
  padding: 12px;
  background: #42b883;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.25s, opacity 0.2s;
}
.submit-btn:disabled {
  background: #b0c4de;
  cursor: not-allowed;
  opacity: 0.7;
}
.submit-btn:not(:disabled):hover {
  background: #2f9d72;
}
.success-message {
  margin-top: 20px;
  padding: 12px;
  background: #e8f8f0;
  color: #1e7e5a;
  border-radius: 8px;
  text-align: center;
  font-weight: 500;
  border-left: 4px solid #42b883;
}
</style>