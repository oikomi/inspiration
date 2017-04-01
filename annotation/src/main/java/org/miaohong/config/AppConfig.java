package org.miaohong.config;

import org.miaohong.annotation.DatabaseType;
import org.miaohong.model.JdbcUserDAO;
import org.miaohong.model.MongoUserDAO;
import org.miaohong.model.UserDao;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

/**
 * Created by miaohong on 17/4/1.
 */
@Configuration
@ComponentScan
public class AppConfig {
    @Bean
    @DatabaseType("MONGO")
    public UserDao mongoUserDAO(){

        return new MongoUserDAO();
    }

    @Bean
    @DatabaseType("MYSQL")
    public UserDao jdbcUserDAO(){

        return new JdbcUserDAO();
    }

}
