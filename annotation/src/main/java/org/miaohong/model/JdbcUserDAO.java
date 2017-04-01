package org.miaohong.model;

import java.util.Arrays;
import java.util.List;

/**
 * Created by miaohong on 17/4/1.
 */
public class JdbcUserDAO implements UserDao
{
    @Override
    public List<String> getAllUserNames()
    {
        System.out.println("**** Getting usernames from RDBMS *****");
        return Arrays.asList("Siva","Prasad","Reddy");
    }
}
